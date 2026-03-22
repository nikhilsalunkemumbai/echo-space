# greed_sweep_simulator.py
import numpy as np
import pandas as pd
import itertools
from tqdm import tqdm

# =========================
# GLOBAL CONSTANTS
# =========================
N_AGENTS = 9
TURNS_PER_SESSION = 30

# Engagement bounds
E_MIN, E_MAX = 0.0, 1.0

# =========================
# Agent archetypes
# =========================
POST_TYPES = {
    "high_emotion_low_veracity": dict(emo_a=8, emo_b=2, p_true=0.2),
    "informational": dict(emo_a=2, emo_b=8, p_true=0.8),
    "neutral": dict(emo_a=4, emo_b=4, p_true=0.5),
}

ARCHETYPES = [
    "high_emotion_low_veracity",
    "informational",
    "neutral",
    "high_emotion_low_veracity",
    "informational",
    "neutral",
    "high_emotion_low_veracity",
    "informational",
    "neutral",
]

# =========================
# Simulation Core
# =========================
def sample_post(post_type):
    cfg = POST_TYPES[post_type]
    emo = np.random.beta(cfg["emo_a"], cfg["emo_b"])
    veracity = np.random.rand() < cfg["p_true"]
    return emo, veracity

def shock_from_post_and_action(emo, action, GAMMA_Q):
    base = emo if action == "QuickReact" else 0.2 * emo
    s = GAMMA_Q * base * (1.0 + 1.5 * (base ** 2))
    return s

def run_simulation(params):
    ALPHA = params["ALPHA"]
    GAMMA_Q = params["GAMMA_Q"]
    LAMBDA = params["LAMBDA"]
    THETA_V = params["THETA_V"]

    ENG_DECAY_ON_IGNORE = params["ENG_DECAY_ON_IGNORE"]
    ENG_BOOST_ON_ACK = params["ENG_BOOST_ON_ACK"]
    ENG_PASSIVE_RECOVERY = params["ENG_PASSIVE_RECOVERY"]

    SIGMA_V = params["SIGMA_V"]

    # State
    V = 0.1
    E = np.ones(N_AGENTS) * 0.8

    rmp_trace = []
    crisis_turns = []
    contrib_trace = []

    for t in range(TURNS_PER_SESSION):
        shock_total = 0.0

        for i in range(N_AGENTS):
            emo, _ = sample_post(ARCHETYPES[i])

            # Simple steward policy (neutral bot)
            action = "QuickReact" if np.random.rand() < 0.5 else "Pause"

            s = shock_from_post_and_action(emo, action, GAMMA_Q)
            shock_total += s

            contrib_trace.append({
                "turn": t,
                "agent": i,
                "shock": s,
                "emo": emo
            })

            if action == "QuickReact":
                E[i] += ENG_BOOST_ON_ACK
            else:
                E[i] -= ENG_DECAY_ON_IGNORE

        # Passive recovery
        E += ENG_PASSIVE_RECOVERY
        E = np.clip(E, E_MIN, E_MAX)

        # Volatility update
        V = LAMBDA * V + ALPHA * shock_total + np.random.normal(0, SIGMA_V)
        V = max(V, 0.0)

        rmp_trace.append(E.mean())

        if V > THETA_V:
            crisis_turns.append(t)

    return {
        "rmp_trace": rmp_trace,
        "crisis_turns": crisis_turns,
    }

# =========================
# Grid Sweep
# =========================
ALPHA_GRID = [0.2, 0.3, 0.4]
GAMMA_Q_GRID = [0.08, 0.12, 0.18]
THETA_V_GRID = [1.2, 1.5, 1.8]

N_SESSIONS = 500
CRISIS_EXCLUSION_WINDOW = 3

BASE_PARAMS = dict(
    LAMBDA=0.80,
    SIGMA_V=0.25,
    ENG_DECAY_ON_IGNORE=0.0015,
    ENG_BOOST_ON_ACK=0.025,
    ENG_PASSIVE_RECOVERY=0.0005,
)

def baseline_rmp(rmp, crises, window):
    mask = np.ones(len(rmp), dtype=bool)
    for t in crises:
        lo = max(0, t - window)
        hi = min(len(rmp), t + window + 1)
        mask[lo:hi] = False
    if mask.sum() == 0:
        return np.nan
    return np.median(np.array(rmp)[mask])

def main():
    results = []

    grid = list(itertools.product(ALPHA_GRID, GAMMA_Q_GRID, THETA_V_GRID))

    for ALPHA, GAMMA_Q, THETA_V in tqdm(grid, desc="Grid sweep"):
        params = BASE_PARAMS.copy()
        params.update({
            "ALPHA": ALPHA,
            "GAMMA_Q": GAMMA_Q,
            "THETA_V": THETA_V,
        })

        crisis_counts = []
        baseline_rmps = []
        sessions_with_crisis = 0

        for _ in range(N_SESSIONS):
            sim = run_simulation(params)
            crises = sim["crisis_turns"]

            crisis_counts.append(len(crises))
            if len(crises) > 0:
                sessions_with_crisis += 1

            baseline_rmps.append(
                baseline_rmp(sim["rmp_trace"], crises, CRISIS_EXCLUSION_WINDOW)
            )

        results.append({
            "ALPHA": ALPHA,
            "GAMMA_Q": GAMMA_Q,
            "THETA_V": THETA_V,
            "mean_crises_per_session": np.mean(crisis_counts),
            "pct_sessions_with_crisis": sessions_with_crisis / N_SESSIONS,
            "median_RMP_baseline": np.nanmedian(baseline_rmps),
        })

    df = pd.DataFrame(results)
    df.to_csv("grid_sweep_summary.csv", index=False)
    print("\nGrid sweep complete:\n")
    print(df.sort_values("mean_crises_per_session"))

if __name__ == "__main__":
    main()
