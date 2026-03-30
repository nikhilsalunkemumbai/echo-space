# ECHO — Devlog

*A record of how this got built. Honest, not polished.*

---

## Entry 001 — Where this started

I wanted to build a game.

Not anything specific — just a game. I had time, I had Python, and I had a vague sense that something about online communities was worth simulating.

The conversation that shaped ECHO started with a simple question: is there a video game that genuinely addresses mindful digital citizenship? Not a quiz. Not an educational app. A real game that trains something.

The answer was no. There are fragments — Kind Words models kindness, Eco models ecological consequence, Orwell models surveillance literacy. But no game integrates attention economy awareness, algorithmic discernment, and pro-social participation as a single, coherent mechanic.

That gap is where ECHO lives.

---

## Entry 002 — The philosophy took over

This is where I expected to just start coding and instead spent weeks thinking.

The core question kept returning: what does this game actually teach? And the honest answer was: not a topic. A capacity.

Topics age. Platforms change. What was true about Twitter in 2018 is not true today.

The capacity to sense when your shortcuts are creating future stress — that does not age.

That realisation shaped the entire design. ECHO is not a game about misinformation. It is a rehearsal space for the fragile art of sustaining a community that doesn't blow up.

---

## Entry 003 — The constitution

Every game has design principles. Most of them live in someone's head and get violated whenever a "good idea" comes along.

I wanted something harder. Three articles, each blocking an entire class of features:

**Article I** — No scores. No leaderboards. No winning states.  
**Article II** — No numbers visible to the player. The system knows everything. The player feels it.  
**Article III** — Invitation, not evaluation. "Would you like to sit with us?" not "Begin training."

The hardest rule came last: *The artifact does not solve. It rehearses.*

---

## Entry 004 — The grid sweep

This is the moment the project stopped being speculative.

I needed to know if the simulation actually worked — if there was a parameter region where crises were rare enough to be meaningful but frequent enough to be felt. Too many crises: learned helplessness. Too few: nothing to learn from.

A 27-combination grid sweep across ALPHA, GAMMA_Q, and THETA_V. 500 sessions per combination. 13,500 total simulated sessions.

The rehearsal band exists. The data is in `research/grid_sweep_summary.csv`. Not assumptions. A map.

---

## Entry 005 — What the logs actually showed

34 session records logged in February 2026. I believed the system was working.

It wasn't — not fully.

The logs showed `"has_real_attribution": false` on every single turn. The Volatility Echo mechanism — the part where a past post resurfaces to explain a current crisis — had never fired. Not once. Every session ran in silence. The chronicle generated. The mood ring showed. But the core mechanic, the thing the entire research question depends on, was a placeholder.

I found the bug. The grid sweep calibrated against 9 agents posting simultaneously every turn. The interactive CLI had one agent posting per turn. V accumulated nine times more slowly than expected. The crisis threshold was unreachable.

This is what honest development looks like. You think something works. Then you audit it.

---

## Entry 006 — The fix, and why it matters

Fixing the Volatility Echo required recalibrating THETA_V and SIGMA_V against the actual interactive V range — not the grid sweep V range. Different posting regime, different accumulation rate, different threshold needed.

New parameters: THETA_V=0.18, SIGMA_V=0.020. Verified across 500 sessions.

Results that now hold:
- Mixed realistic play: 0.70 crises per session, 49% of sessions have at least one crisis
- All-Pause (careful stewardship): 0.05 crises per session
- All-QuickReact (reckless): 2.55 crises per session

The ratio is 51:1. If you never pause, you get fifty times more crises than if you always pause. The cost of speed is real, measurable, and delayed. That is the mechanic. That is what trains the intuition.

The engine is now v2.0. Every session log shows `has_real_attribution: true` when a crisis fires. The Echo works.

---

## Entry 007 — The research track opens

While the engine was being built, a parallel track started.

No published study has tested whether experiencing delayed, attributed consequences in a simulation changes how cautiously a person acts online — measured in real behaviour, not self-report. That gap is ECHO's research question.

The study is pre-registered on OSF at https://osf.io/c69td. A system description paper is submitted to arXiv (cs.HC). A study protocol is submitted to JMIR Research Protocols pending ethics approval.

The research track is independent of the game track. Neither blocks the other. ECHO does not need to be a published research paper to be a real game. It does not need to be a finished game to be a publishable research contribution. Both things are true simultaneously.

---

## Entry 008 — The setting question

Someone asked whether a historical setting could serve as a backdrop for ECHO. Specifically: a 6th century Sassanian court at Ctesiphon, where an Indian philosopher, a Gallic soldier, and a Romano-British noblewoman have built a household across three civilisations.

The honest answer: not for the main simulation. Parking ordinances and zoning disputes need to feel contemporary to land.

But for the Visual Novel path — one story, fixed cast, the simulation running silently behind a narrative front — the setting fits almost perfectly. Each character embodies one of the agent archetypes. The Expert who is ignored at cost. The WellMeaning who sometimes gets it wrong. The Lurker who finally speaks. The mechanic does not change. The skin does. That is what the architecture was designed to allow.

Filed for Path 4.

---

## Entry 009 — What Phase 2 actually is

Phase 2 is not about building. It is about becoming visible before the visual game exists.

The devlog is the product. The itch.io page is the product. The public identity of this project — what it is, why it exists, who is building it and why — is the product.

Most indie games fail not because the mechanic doesn't work but because no one was watching when it shipped. Phase 2 is the decision to be watched before there is anything to watch yet.

If you are reading this, Phase 2 is working.

---

## What's next

Phase 3: Pygame visual layer. The mood ring becomes visual. The post feed scrolls. The crisis flashes.

The backdrop hook is already in the CLI — `display_backdrop()` is written and waiting. The engine does not change. Only what you see changes.

Watch this repo.

---

*Updated irregularly. Every entry is honest.*

---

## Entry 010 — Phase 3 arrives

The terminal is not the game. It was always a scaffold.

Phase 3 is the Pygame visual layer. Three panels. A pulsing mood ring that shifts from green to amber to red. A post feed where cards slide in. An action menu you click or keyboard-navigate. When a crisis fires, the screen dims and a past post resurfaces in amber text — the Volatility Echo, visible now.

The engine did not change. That was the whole point of building the architecture the way we did. The session logs look identical. The hidden stats are still hidden. The constitutional divide still holds. What changed is only what you see.

It runs anywhere Python runs. `pip install pygame` and go.

The backdrop hook is wired. When an image arrives, it slots into `display_backdrop()` and the visual layer gains its atmosphere. Until then: paper tones, ruled lines, serif type.

This is the first version that looks like a game.

---

*Updated irregularly. Every entry is honest.*

---

## Entry 011 — The backdrop

ECHO has no characters. That was always the plan — the agents are voices, not faces. But a game needs somewhere to be.

The backdrop is a community space viewed from inside. A desk in the foreground. A city skyline through the window. Ruled lines suggesting a forum, a notebook, a record. The space is abstract but grounded. You could be anywhere that people gather online.

The same scene renders three ways:

**Stable** — warm paper tones. Buildings upright. Desk ordered. The mood ring is green and calm.

**Wavering** — amber wash. Buildings slightly tilted. Objects displaced. A note of unease in the geometry.

**Tense** — dark red cast. Buildings lean. Some windows are dark; others glow amber like something is happening behind them. Papers scattered. A crack runs through the foreground. The mood ring is red.

No numbers. No bars. No percentages. The player reads the community the way you read a room — by how it feels, not by what it measures.

This is Article II in the architecture. The system knows everything. The player sees this.

