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

The rehearsal band exists. ALPHA=0.3, GAMMA_Q=0.12, THETA_V=1.5. About 0.94 crises per session. 36.6% of sessions have at least one crisis. The system has physics.

The data is in `research/grid_sweep_summary.csv`. Not assumptions. A map.

---

## Entry 005 — First sessions logged

34 real sessions logged on 8 February 2026 with the CLI interface.

The Chronicle works. The mood ring works. The crisis replay works — a past post resurfaces with amplified emotional language, and a quiet caption: "An earlier tension resurfaces in the community now."

Hidden stats logging correctly. Observable state correctly abstracted. The constitutional divide holds in code.

This is real now.

---

## Entry 006 — The research question

The design conversations raised a question I couldn't ignore.

No published study has tested whether experiencing delayed, attributed consequences in a simulation changes how cautiously a person acts online — measured in real behavior, not self-report.

That is ECHO's research question. The inoculation games (Bad News, Go Viral!) test whether you can spot manipulation. The Be Internet Awesome RCT found no behavioral change from a digital citizenship curriculum. Neither tests behavioral tempo — the time between encountering a post and choosing how to react.

ECHO tests that. And nobody else has.

A system description preprint is on arXiv. A study protocol is in ethics review. The research question is pre-registered on OSF.

---

## What's next

Phase 3: Pygame visual layer. The first version that doesn't run in a terminal.

If you want to follow along, watch this repo.

---

*Updated irregularly. Every entry is honest.*
