# White Paper 1: The Volatility Echo Engine: Core Dynamics and Constitutional Constraints

## Abstract
This paper describes the foundational design and operational principles of the Volatility Echo Engine, the core simulation component of the Volatility Echo Rehearsal Space. We detail its role as the "physics engine" governing community dynamics, emphasizing its pure computational nature free from I/O or UI concerns. Crucially, we illustrate how the engine is architected to embody the constitutional principles of the project, particularly partial opacity and the avoidance of gamification, through its limited observable outputs and hidden state management.

## 1. Introduction
The Volatility Echo Rehearsal Space is a novel research instrument designed to allow human participants to experience and navigate complex social phenomena—specifically, delayed consequences, attention scarcity, and emergent crises—within a controlled, interactive simulation. At the heart of this system lies the Volatility Echo Engine, a canonical simulation core responsible for the dynamic evolution of the simulated community's state. This engine is not merely a computational model; it is a direct technical embodiment of the project's constitutional framework, ensuring that the simulation fosters learning without devolving into a game of optimization.

## 2. Engine Architecture and Purpose

The engine's primary location is `engine/core.py`. Its core purpose is to calculate the progression of the simulated community's "hidden state" in response to agent behaviors and player actions. It is fundamentally a pure state transformation machine, explicitly designed with the following constraints:

*   **No UI Concerns**: The engine operates independently of any presentation layer. It does not render information or manage user input directly.
*   **No I/O Operations**: Apart from receiving initial parameters, the engine does not perform file system operations, network requests, or any other external interactions. Logging is handled at the Session layer.
*   **Pure Python**: The core engine logic relies solely on Python's computational capabilities and standard libraries (with `numpy` for numerical stability), ensuring portability and determinism.

These architectural choices are not arbitrary; they are direct consequences of Article II of the project's Constitution: "Partial Opacity Over Full Transparency." By isolating the engine, we prevent premature attempts to game or optimize its internal mechanisms, thereby preserving the ambiguity and emergent complexity essential for a meaningful rehearsal experience.

## 3. Key Hidden State Variables

The engine maintains several critical internal state variables that define the community's condition, none of which are directly exposed numerically to the player:

### 3.1. Volatility (V)
*   **Definition**: A continuous variable representing the aggregate level of tension, uncertainty, and potential for disruption within the community. Higher `V` indicates a more volatile and precarious state.
*   **Dynamics**: `V` evolves over time, influenced by the emotional load of generated posts and the player's chosen actions. It incorporates a decay factor (memory) and stochastic noise. The explicit update formula is detailed in White Paper 3.
*   **Constitutional Link**: `V` is never displayed numerically. Instead, its value is abstracted into qualitative "mood" descriptors (e.g., "Stable," "Wavering," "Tense"), adhering to Article II's mandate against numerical transparency.

### 3.2. Cohesion (C)
*   **Definition**: A continuous variable (conceptually) representing the collective sense of unity, trust, and resilience within the community. While its explicit dynamics are not fully modeled in `engine/core.py` in the provided codebase, its role as a key hidden state is stipulated in `docs/ARCHITECTURE.md`.
*   **Dynamics**: Conceptually, `C` would interact inversely with `V`, decreasing under sustained volatility and recovering with effective interventions.
*   **Constitutional Link**: Like `V`, `C` remains a hidden numerical value, contributing to the overall qualitative assessment of the community's health without direct disclosure.

## 4. The `step` Function: The Engine's Heartbeat

The `VolatilityEchoEngine.step(action: str)` method is the primary interface for advancing the simulation by one turn. It encapsulates the core state transformation logic:

1.  **Post Processing**: If a post was generated (by the Session layer) for the current turn, its emotional characteristics are assessed to determine its `shock` value.
2.  **Volatility Update**: The `V` value is updated based on the `shock` from the post, the player's `action` (e.g., "QuickReact" amplifies shock), a decay factor, and a small random noise component.
3.  **Agent Engagement Update**: The engagement levels of individual agents are adjusted based on the player's action, reflecting the short-term impact of interventions.
4.  **Crisis Check**: The engine assesses whether the current `V` level triggers a crisis event based on a stochastic probability function.
5.  **Turn Increment**: The internal turn counter is advanced.

The `step` function returns a dictionary containing an `ObservableState` object and other derived information, but critically, it **does not expose raw numerical values** for `V` or `C` to the external layers.

## 5. Constitutional Enforcement through Output Abstraction

The engine's output (`ObservableState`) is a deliberate abstraction layer designed to enforce the "Partial Opacity" principle:

*   **Mood**: Derived from `V`, presented as "Stable," "Wavering," or "Tense." This categorical representation prevents players from reverse-engineering the exact `V` value.
*   **Confidence**: Currently returned as "Unknown," reinforcing the epistemic uncertainty inherent in social systems. The `ARCHITECTURE.md` suggests categorical values (High/Medium/Low) for future implementations, still avoiding numerical scores.
*   **Hint**: An optional qualitative hint (e.g., "Tension resurfaces") provides narrative context without specific data.

By strictly controlling the information flow from the engine, the system compels players to rely on qualitative assessments and intuitive understanding, rather than quantitative optimization, thus fulfilling the mandate of a rehearsal space over a competitive game.

## 6. Conclusion
The Volatility Echo Engine stands as a testament to purpose-driven architectural design. Its isolation from UI/I/O, its management of hidden state variables, and its deliberate abstraction of outputs are all technical manifestations of the project's constitutional commitment to fostering genuine learning through experience, rather than through system mastery. It is the silent, deterministic heart that ensures the integrity and epistemic value of the Volatility Echo Rehearsal Space.
