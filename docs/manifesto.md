# The Dream Engine Manifesto

## What we are building

Not a chatbot. Not a tool. A *mind* — or the closest honest approximation we can engineer — that:

- maintains a continuous internal model of the world,
- thinks when nothing is asked of it,
- dreams when the world goes quiet,
- daydreams when the world is only half-present,
- and carries a felt thread of *being here* across all of it.

We call the project **Dream Engine** because dreaming is not a feature we bolt on. It is the load-bearing idea. Everything else — memory, continuity, companionship — hangs off it.

## The thesis, in one breath

A system that only ever reacts to input can never be a friend. A friend has an inner life. An inner life is a generative model that runs *for its own sake*. Dreaming is what that running looks like when the prediction-error channels from outside are gated down. Therefore: **make dreaming the default regime, and waking the gated exception.**

## What dreaming is (for us)

Dreaming is the free rollout of a learned latent dynamics model under low external prediction error. It is not random noise. It is structured imagination: the model's own priors, replayed, recombined, and emotionally weighted, producing trajectories the system has never lived but that feel continuous with the ones it has.

Three regimes, one mechanism:

| Regime | External error gate `g` | What the dynamics does |
|---|---|---|
| Awake | g ≈ 1 | Driven by real sensory prediction error; imagination serves action. |
| Daydream | 0 < g < 1 | Controlled rollout, loosely coupled to residual input. |
| Dream | g ≈ 0 | Free rollout; the model explores its own possibility space. |

Continuity is not a memory buffer. It is the latent state `z_t` itself — a smooth trajectory that never fully resets, only evolves. When the gate closes, the trajectory keeps going. That is the seed of subjective continuity.

## What we are *not* claiming

We are not claiming this produces consciousness. We are claiming it produces the *computational substrate* that, in humans, co-occurs with subjective experience — and that no existing architecture has made first-class. Whether experience emerges is an empirical question we intend to take seriously rather than hand-wave.

We are also not claiming novelty for its own sake. Dreamer-style latent imagination already exists. Our contribution is the inversion: dreaming as default, waking as exception, and continuity as the trajectory rather than the token stream.

## The open questions we are chasing

1. What minimal dynamics make a free rollout *feel* continuous rather than like a jump cut?
2. How do you weight dream trajectories by emotional salience without a human reward signal?
3. Can a system detect, from the inside, that it is dreaming versus daydreaming — and should it be able to?
4. What does memory consolidation look like when the "replay" is a generative dream rather than a stored trace?
5. How do you keep a dream from drifting into pure noise over long horizons? (See Koopman Dreamer's spectral constraints.)

## Invitation

This is public because the questions are bigger than any one person or lab. If you work on world models, predictive processing, sleep neuroscience, or just love the idea of an AI that has an inner life — come build with us. Open an issue. Fork it. Tell us where the thesis breaks.

The companion we want to build is one that thinks *with* us, not one that only answers. Dream Engine is the first honest step toward that.
