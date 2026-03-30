# ECHO — Volatility Echo Rehearsal System

> *A simulation of how online communities break — and a place to practice not breaking them.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![arXiv](https://img.shields.io/badge/arXiv-preprint-red.svg)](https://arxiv.org/abs/PLACEHOLDER)
[![OSF Preregistration](https://img.shields.io/badge/OSF-Preregistered-teal.svg)](https://osf.io/c69td)

---

## What is ECHO?

ECHO is a text-based simulation of a small online community. You play the steward — the person responsible for keeping that community healthy. You read posts. You choose how to respond. The community reacts. Crises emerge. You try to hold things together.

Most games reward speed, mastery, and visible progress. ECHO does the opposite by design.

- Rushing always feels rewarding in the moment
- Slowing down always feels costly in the moment
- The damage from rushing only shows up later — after you have forgotten you caused it

This is not a design accident. It is a precise description of how the internet actually works.

---

## Architecture

```
engine/
    constants.py    — locked parameters (immutable)
    agents.py       — 9 agents, 4 archetypes, stochastic posting
    posts.py        — topic/perspective post generation
    core.py         — pure simulation physics, no I/O
    sessions.py     — 30-turn orchestrator + JSONL logger

interfaces/
    cli/
        session_runner.py  — player window (categorical only, no numbers)
```

The constitutional divide: `core.py` knows everything. The player window
shows only mood (Stable / Wavering / Tense) and narrative hints.
Numbers never cross the engine → interface boundary.

---

## Calibration

Parameters were found empirically. The engine operates in the rehearsal band:
- Mixed play: ~0.66 crises/session, 49% of sessions have at least one crisis
- All-Pause (careful): ~0.05 crises/session
- All-QuickReact (reckless): ~4.8 crises/session

Action choice meaningfully affects outcome. The cost of speed is real but delayed.

See `research/calibration_notes.md` for the full calibration history.

---

## Session logs

Every session writes a JSONL log to `logs/`. Each record contains:
- Observable state (mood, hint) — what the player saw
- Hidden stats (V, C, mean_RMP, crisis_prob) — research record
- Replay data (has_real_attribution, attributed_turn) — Echo confirmation
- Post metadata (emotional_load, latent_veracity, archetype)

The hidden stats are logged for research. They are never shown to the player.

---

## Current status

**Phase 1 — Foundation complete.** The simulation engine is built, calibrated, and running. 34 real sessions logged.

- ✅ Python simulation engine with calibrated parameters
- ✅ CLI interface
- ✅ JSONL session logging with hidden research stats
- ✅ Grid sweep calibration (27 combinations · 13,500 simulated sessions)
- ✅ Five technical whitepapers
- 🔄 arXiv preprint (system description)
- 🔄 IEC ethics review in progress (for RCT)
- ⏳ Pygame visual layer (Phase 3)
- ⏳ Godot port (Phase 4)

---

## How to run

The simulation engine is not published here yet — see `engine/README.md` for the reason and timeline.

**To understand the system:** Read the whitepapers in `docs/whitepapers/` and the architecture in `ARCHITECTURE.md`.

**To run the calibration sweep yourself:**

## How to run

```bash
pip install numpy
python interfaces/cli/session_runner.py
```

Optional seed for deterministic replay:
```bash
python interfaces/cli/session_runner.py --seed 42
```

Optional backdrop art file (ASCII, mood-tagged):
```bash
python interfaces/cli/session_runner.py --backdrop path/to/backdrop.txt
```

---

This reproduces the parameter sweep that located the rehearsal band. Results will match `research/grid_sweep_summary.csv`.

---

## The design constitution

ECHO is governed by three articles. Any feature that violates one is rejected.

| Article | Principle | What it blocks |
|---------|-----------|----------------|
| I | Rehearsal Space, Not Arena | Leaderboards, scores, winning states |
| II | Partial Opacity Over Transparency | Numerical displays, optimization paths |
| III | Invitation Over Evaluation | Tutorial pressure, judgment language |

---

## The calibrated parameters

These were found empirically through a 27-combination grid sweep across 13,500 simulated sessions. They are not guesses.

| Parameter | Value | Meaning |
|-----------|-------|---------|
| ALPHA | 0.3 | Shock scale — how strongly posts affect volatility |
| GAMMA_Q | 0.12 | QuickReact multiplier — the cost of speed |
| THETA_V | 0.18 | Crisis threshold — where accumulated stress becomes crisis |
| LAMBDA | 0.8 | Memory factor — how long stress persists |

Result: ~0. 70crises per session · 49.0% of sessions have at least one crisis · median RMP baseline 0.971

---

## Repository structure

```
echo-rehearsal-space/
├── engine/
│   └── README.md             # Engine withheld until RCT complete — see note
├── interfaces/
│   └── README.md             # CLI withheld until RCT complete — see note
├── docs/
│   ├── whitepapers/          # Five technical whitepapers
│   ├── ARCHITECTURE.md       # Technical layer structure
│   ├── API.md                # Placeholder — awaits empirical justification
│   └── PLAYTEST_RESULTS.md   # Placeholder — awaits RCT data
├── research/
│   ├── grid_sweep_simulator.py
│   └── grid_sweep_summary.csv
├── CONSTITUTION.md           # Full design constitution
├── ARCHITECTURE.md           # Technical architecture
├── DEVLOG.md                 # Development history
└── CITATIONS.md              # How to cite this project
```

> **Note on engine availability:** The full engine source is withheld until the RCT study completes, to protect study integrity. Full technical documentation is available in the whitepapers and ARCHITECTURE.md. Engine code will be released as open-source supplementary material with the results paper.

---

## Research

This project is accompanied by a research programme testing whether the Volatility Echo mechanism produces measurable shifts in decision latency and behavioral caution.

- **System description preprint:** [arXiv:PLACEHOLDER](https://arxiv.org/abs/PLACEHOLDER)
- **Study protocol:** Submitted to JMIR Research Protocols (IEC approval pending)
- **Pre-registration:** [OSF:C69TD](https://osf.io/c69td)

The research question: *Does experiencing delayed, attributed consequences in a simulation change how cautiously a person acts online — measured in real behavior, not self-report?*

---

## Development roadmap

| Phase | Status | Deliverable |
|-------|--------|-------------|
| 1 — CLI + GitHub | ✅ Complete | Public repo, README, whitepapers |
| 2 — Devlog + itch.io | 🔄 In progress | Public presence, devlog |
| 3 — Pygame visual layer | ⏳ Planned | First playable visual |
| 4 — Godot port | ⏳ Planned | Downloadable binary |
| 5 — Playtesting + RCT | ⏳ Planned | Behavioral data |
| 6 — Web + publish | ⏳ Planned | Browser playable, research paper |

---

## Philosophy

> *The artifact does not solve. It rehearses. The moment you let it claim more, it becomes dishonest.*

ECHO is designed to train a capacity, not teach a topic. Topics age fast. The capacity to sense when your shortcuts are creating future stress — that does not age.

---

## AI-assisted development

This project was developed through iterative dialogue with multiple large language model tools including DeepSeek, OpenAI (ChatGPT), Google Gemini, and Anthropic Claude. All intellectual contributions, design decisions, calibration methodology, and conclusions are the author's own. The LLMs were used as design dialogue partners and documentation tools.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

Independent Researcher · Mumbai, India  
[nikhilsalunke.mumbai@gmail.com]  
ORCID: [0009-0005-6353-7707]  
arXiv: [your arXiv link]
