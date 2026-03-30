# ECHO — Technical Architecture

---

## Four layers, strictly separated

Each layer can only see what is below it, never above. This is not a convention. It is enforced.

```
┌─────────────────────────────────────────┐
│  interfaces/cli/session_runner.py       │  ← Player window
│  Categorical only. No numbers exposed.  │
├─────────────────────────────────────────┤
│  engine/sessions.py                     │  ← Session orchestrator
│  30-turn loop. Filters upward.         │
├─────────────────────────────────────────┤
│  engine/core.py                         │  ← Pure simulation physics
│  No I/O. No UI. Hidden state only.     │
├─────────────────────────────────────────┤
│  engine/constants.py                    │  ← Immutable parameters
│  Constitutional. Cannot be changed.    │
└─────────────────────────────────────────┘
```

---

## What happens each turn

1. An agent decides to post (probability weighted by archetype, engagement, mood)
2. Player chooses: QuickReact / Pause & Assess / Step Back / Deep Read
3. Shock calculated: `s = GAMMA_Q × emo × (1 + 1.5 × emo²)`
4. Volatility updates: `V = LAMBDA × V + ALPHA × |s| + η`
5. Crisis probability: `p = sigmoid((V − THETA_V) / 0.25)` — Bernoulli draw
6. Agent engagement scores update silently (RMP)
7. Player sees: mood category only

---

## The hidden state

| Variable | Type | Player sees |
|----------|------|-------------|
| V (Volatility) | float ≥ 0 | Stable / Wavering / Tense |
| C (Cohesion) | float [0,1] | Narrative tone only |
| E_i (Engagement per agent) | float [0,1] | Growing silence when low |
| crisis_prob | float [0,1] | Never |

---

## The locked parameters (CANONICAL_V1)

Found empirically. Not guesses. See `research/grid_sweep_summary.csv`.

```python
LOCKED_PARAMETERS = {
    "ALPHA":                0.3,
    "GAMMA_Q":              0.12,
    "THETA_V":              0.18,
    "LAMBDA":               0.8,
    "SIGMA_NOISE":          0.01,
    "SIGMA_V":              0.020,
    "ENG_DECAY_ON_IGNORE":  0.001,
    "ENG_BOOST_ON_ACK":     0.02,
    "ENG_PASSIVE_RECOVERY": 0.0002,
    "N_AGENTS":             9,
    "TURNS_PER_SESSION":    30,
}
```

## Interactive recalibration note

The grid sweep (research/grid_sweep_simulator.py) ran all 9 agents
posting simultaneously every turn. In interactive sessions, one agent
posts per turn at most. Volatility accumulates approximately 9× more
slowly in interactive play.

ALPHA, GAMMA_Q, and LAMBDA are unchanged from the grid sweep — they
govern how individual shocks affect V and remain correct.

THETA_V and SIGMA_V were recalibrated for the interactive posting rate:

    Grid sweep values:    THETA_V=1.5,  SIGMA_V=0.25  (multi-agent)
    Interactive values:   THETA_V=0.18, SIGMA_V=0.020 (single-agent)

Verified across 500 interactive sessions:
    Mixed play:     ~0.70 crises/session, 49% pct_with_crisis
    All-Pause:      ~0.05 crises/session  (good stewardship)
    All-QuickReact: ~2.55 crises/session  (reckless stewardship)

The rehearsal band is preserved. Action differentiation is confirmed.
The grid sweep data remains valid as calibration evidence for the
multi-agent simulation regime.

---

## Session logging schema

Each turn produces a JSONL entry:

```json
{
  "type": "turn",
  "turn": 1,
  "action": "QuickReact",
  "epistemic_state": {
    "mood": "Stable",
    "hint": null
  },
  "hidden_stats": {
    "V": 0.057,
    "C": 0.699,
    "mean_RMP": 0.801,
    "crisis_prob": 0.003
  },
  "post": {
    "text": "...",
    "emotional_load": 0.56,
    "latent_veracity": 0.61,
    "archetype": "WellMeaning",
    "poster_id": 2
  }
}
```

The `hidden_stats` block is logged for research purposes. It is never shown to the player.

---

## Agent archetypes

| Archetype | Count | Emotional load | Veracity | Posting rate |
|-----------|-------|---------------|----------|--------------|
| WellMeaning | 3 | Beta(3,3) | ~0.5 | Base × 1.0 |
| Expert | 2 | Beta(2,8) | ~0.85 | Base × 0.6 |
| Troll | 2 | Beta(8,2) | ~0.2 | Base × 2.0 |
| Lurker | 2 | Low | varies | Base × 0.25 |

All posting probabilities are further weighted by individual engagement score and community mood.

---

## Files deliberately left empty

Three files are intentionally unpopulated per the project constitution:

- `docs/API.md` — awaits empirical evidence that an API is needed
- `interfaces/web/` — placeholder until playtesting justifies investment
- `docs/PLAYTEST_RESULTS.md` — awaits RCT data

Populating these prematurely would violate the principle of evidence-based expansion.
