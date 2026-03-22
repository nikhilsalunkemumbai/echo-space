# White Paper 2: Modeling Community Response: Agent Behavior and Post Generation in Volatility Echo

## Abstract
This paper details the mechanisms by which community engagement and content generation are modeled within the Volatility Echo Rehearsal Space, focusing on the `Agent`, `AgentManager`, and `GeneratedPost` components. We elucidate how these elements simulate diverse community member archetypes, their stochastic posting behaviors influenced by internal states and community mood, and the attributes of the posts they generate. This model serves as the primary source of emergent behavior and input for the core simulation engine, reflecting the constitutional emphasis on realistic, non-predictable social dynamics.

## 1. Introduction
A crucial aspect of simulating a digital community is the credible representation of its members and their interactions. In the Volatility Echo Rehearsal Space, this is achieved through a multi-agent system comprising `Agent` entities managed by an `AgentManager`, which collectively generate `GeneratedPost` objects. These components are responsible for creating the dynamic flow of information and sentiment that the player observes and reacts to, forming the "community response" layer atop the engine's physics.

## 2. Agent Archetypes and Characteristics

The simulation incorporates several distinct `Agent` archetypes, each possessing unique behavioral biases that influence their likelihood to post and the nature of their contributions. These archetypes are defined within the `AgentManager` and reflect common roles found in online communities:

*   **WellMeaning**: Agents with generally positive intentions, contributing constructively.
*   **Expert**: Agents providing factual or authoritative information, potentially with lower emotional load.
*   **Troll**: Agents prone to generating emotionally charged or provocative content.
*   **Lurker**: Agents who primarily consume content and are less likely to post.

Each `Agent` instance possesses:
*   `id`: A unique identifier.
*   `archetype`: Their assigned behavioral role.
*   `engagement`: A hidden numerical score (0-1) reflecting their current level of activity and investment in the community. This score dynamically updates based on player actions, simulating the responsiveness of community members to interventions.

## 3. Stochastic Posting Behavior

Agents do not post on every turn; their decision to post is stochastic and influenced by two key factors:

### 3.1. `should_post(mood: str)`
This method determines an agent's willingness to contribute in a given turn. It considers:
*   **Community Mood**: As derived qualitatively from the `Volatility (V)` by the `VolatilityEchoEngine` (e.g., "Stable," "Wavering," "Tense"). Agents may have different propensities to post based on the prevailing mood (e.g., "Trolls" might be more active during "Tense" periods).
*   **Individual Engagement (`self.engagement`)**: Agents with higher engagement are generally more likely to post.
*   **Base Probability**: Each mood state has a base probability, which is then modified by the agent's engagement. A random draw against this modified probability determines the posting decision.

### 3.2. `AgentManager.get_posting_agent(community_mood: str)`
The `AgentManager` aggregates these individual decisions. In each turn, it identifies all agents `willing` to post based on their `should_post` method. If multiple agents are willing, one is selected uniformly at random from the willing pool. If no agents are willing, no post is generated for that turn. This mechanism ensures a realistic, sometimes sparse, content flow, reflecting the "attention scarcity" aspect of the simulation.

## 4. Post Generation and Attributes

Once an agent is selected to post, they generate a `GeneratedPost` object. While the `text` of the post is currently a generic placeholder ("A community member raises a concern."), the crucial elements are its associated attributes, which determine its impact on the simulation:

*   **`emotional_load`**: A float representing the intensity of sentiment carried by the post (e.g., 0.2 for low, 0.9 for high). This attribute is a primary driver of `Volatility (V)` updates in the core engine. It is randomly generated within a range (`0.2` to `0.9`) by the `Agent.generate_post_attributes()` method.
*   **`latent_veracity`**: A float representing the underlying truthfulness or accuracy of the post (e.g., 0.3 for low, 0.9 for high). This attribute might be used in future expansions for deeper analysis but currently also randomly generated (`0.3` to `0.9`).
*   **`poster_archetype`**: The archetype of the agent who created the post.
*   **`poster_id`**: The unique ID of the posting agent.
*   `topic` and `perspective`: Currently generic, but designed for future expansion to add narrative depth.

The generation of these attributes, particularly `emotional_load`, is central to how agent actions translate into changes in the community's state.

## 5. Dynamic Engagement Update

The player's actions have a direct and immediate impact on agent `engagement` levels via the `AgentManager.update_engagement(agent_id: int, delta: float)` method. For instance, a "QuickReact" action, while intended to address an issue, might decrease the engagement of the posting agent (`delta = -0.05`), simulating a negative reaction to an overly swift or unnuanced response. Conversely, other actions might increase engagement. This feedback loop ensures that the community model is responsive to the player's interventions, adding a layer of strategic depth to the rehearsal.

## 6. Conclusion
The agent behavior and post generation models within Volatility Echo provide the dynamic, human-centric input that drives the simulation. By defining diverse archetypes, implementing stochastic yet mood- and engagement-dependent posting logic, and assigning crucial impact attributes to generated content, the system creates a believable and challenging environment. This intricate interplay directly supports the constitutional mandates of the project, ensuring that players confront realistic community responses and the emergent consequences of their actions, fostering a deeper understanding of digital social dynamics.
