# White Paper 4: The Simulation Engine and Its Interfaces: A Constitutional Divide

## Abstract
This paper elucidates the architectural and philosophical distinction between the `VolatilityEchoEngine` and its higher-level interfaces, specifically the CLI rehearsal space. We argue that this constitutional divide is fundamental to the project's integrity, enabling the engine to operate as a pure, comprehensive simulation core while allowing interfaces to selectively present information in a manner consistent with the project's educational and non-gamified objectives. The paper details how the engine generates richer data than is exposed, highlighting the deliberate choices made at the interface layer to enforce partial opacity and foster qualitative understanding.

## 1. Introduction
The Volatility Echo Rehearsal Space is built upon a layered architecture where the core `VolatilityEchoEngine` is deliberately separated from its user-facing interfaces. This separation is not merely a software engineering best practice but a constitutional mandate. The engine (`engine/core.py`) functions as the deterministic "physics" of the simulated community, generating a complete picture of the system's state. In contrast, the various interfaces, such as the current Command-Line Interface (CLI) rehearsal space, act as carefully designed filters, presenting only a subset of the engine's output to the player. This paper explores the rationale and technical implementation of this crucial divide.

## 2. The Comprehensive Engine Core

As described in White Paper 1, the `VolatilityEchoEngine` is a pure state transformation machine. In each `step()`, it computes a comprehensive update to the simulated community's state, including:

*   **Hidden State Variables**: Precise numerical values for `Volatility (V)` and `Cohesion (C)`.
*   **Agent Dynamics**: Individual agent engagement scores and their collective mean (`mean_RMP`).
*   **Crisis Probability**: The exact probabilistic likelihood of a crisis occurring (`crisis_prob`).
*   **Contribution Trace**: A detailed history of posts and their associated shocks (`contrib_trace`).

Crucially, the `step()` method in `engine/core.py` returns a dictionary that includes a `hidden_stats` object, explicitly exposing these raw numerical values internally:

```python
        return {
            "observable_state": ObservableState(
                mood=self._get_mood(),
                confidence="Unknown",
                hint="Tension resurfaces" if crisis else None,
            ),
            "crisis_replay": crisis,
            "processed_post": post,
            "hidden_stats": {
                "V": self.V,
                "C": self.C,
                "mean_RMP": self.agent_manager.get_mean_engagement(),
                "crisis_prob": self._crisis_probability(),
            },
        }
```

This clearly demonstrates that the engine possesses and processes more information than what is typically made available to the end-user through the interfaces.

## 3. The Filtering Role of the Session Layer

The `Session` layer (conceptually represented by `engine/sessions.py` and currently implemented within `interfaces/cli/session_runner.py`) acts as an intermediary. Its primary responsibilities include:

*   **Orchestration**: Managing the 30-turn flow of the simulation.
*   **Agent Interaction**: Requesting posts from the `AgentManager`.
*   **Engine Interaction**: Calling the `engine.step()` method and receiving its full output, including `hidden_stats`.
*   **Logging**: The `Session` layer is responsible for creating a "complete record for The Chronicle" (`session_log`), which may store comprehensive data (including `hidden_stats`) for research purposes.

However, the `Session` layer decides *what information to pass up* to the user-facing interface, already making filtering decisions.

## 4. The Constrained Window of the Interface Layer

The `Interface` layer, exemplified by the `CLISession` in `interfaces/cli/session_runner.py`, is the player's sole window into the simulated world. It receives information from the `Session` layer, but it adheres strictly to the project's constitutional mandates, particularly Article II ("Partial Opacity Over Full Transparency") and Article III ("Invitation Over Evaluation").

### 4.1. Deliberate Obfuscation of Numerical Data

The CLI interface processes the engine's output to present qualitative, non-numerical feedback:

*   **Mood**: Instead of displaying `V` (e.g., "Volatility: 0.73"), the interface presents categorical descriptors like "Stable," "Wavering," or "Tense."
*   **Confidence**: Presented as "Unknown," rather than a precise numerical score.
*   **Crisis Replay**: In v2.0, when a crisis fires, a past post is replayed with an amplified prefix and a neutral narrative caption: "An earlier tension resurfaces in the community now." The player sees which past turn contributed — not who to blame. The attribution is recency-weighted by contribution score, consistent with constitutional partial opacity.

These choices are not limitations of the engine's capabilities but deliberate design decisions to:
*   **Prevent Gamification**: Numeric displays invite optimization and "puzzle-solving," which contradicts the goal of a rehearsal space.
*   **Encourage Qualitative Understanding**: Players are forced to interpret patterns, moods, and narratives, mirroring the ambiguity of real-world social dynamics.
*   **Foster Intuition**: The interface encourages the development of intuition about system state rather than reliance on precise metrics.

## 5. The Rationale for the Divide

The constitutional divide between the comprehensive engine and its constrained interfaces serves several critical purposes:

*   **Epistemic Integrity**: It protects the core simulation from the biases and incentives introduced by user interaction design, ensuring the engine remains a neutral and robust model.
*   **Flexibility for Research**: The engine's ability to output `hidden_stats` allows researchers to access the full quantitative data for analysis, validation, and calibration, while non-research users interact with a pedagogically optimized view.
*   **Enforcement of Principles**: The interface layer acts as a gatekeeper, ensuring that the project's philosophical underpinnings (e.g., rehearsal over game, invitation over evaluation) are enforced at the point of user interaction.

## 6. Conclusion
The architectural separation of the Volatility Echo Engine from its interfaces is a cornerstone of the project's design. This divide ensures that a comprehensive and robust simulation core can operate independently, while the user-facing elements are meticulously crafted to provide an experience that aligns with the constitutional principles of the rehearsal space. By deliberately limiting and abstracting the information presented, the project guides players towards a deeper, qualitative understanding of complex social dynamics, making the interface a pedagogical tool rather than merely a display mechanism.
