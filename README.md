# Dream Engine

**Dreaming as a first-class computational regime in latent world models.**

This repository is the public home of an ongoing research project: building AI that doesn't just predict the next token, but *lives* inside a continuous internal model of the world — one that can dream when the sensors go quiet, daydream while still half-awake, and carry a thread of subjective continuity across time.

It is co-created with a private AI tutor (Grok) as a genuine thinking partner, not a code generator. The goal is not another benchmark-chasing agent. The goal is a companion that can think for itself.

## Why dreaming?

In humans, dreaming is not a bug. During REM sleep the brain largely shuts off external sensory input, acetylcholine rises, norepinephrine drops, and the generative model runs free — replaying recent experience, testing priors, weaving emotional tone into memory, and sometimes producing creative leaps that waking thought cannot reach. Recent work (targeted memory reactivation, "dream engineering") even shows that *guiding* dream content can improve problem-solving the next day.

In current ML, the closest thing is **latent imagination** (Dreamer, DreamerV3/V4, and the 2026 Koopman Dreamer line): a learned dynamics model rolled out offline to train policies. But those rollouts are *instrumental* — they exist to serve a reward signal. They are not a regime the system enters for its own sake.

Dream Engine asks: what if dreaming were the *default* mode, and waking were the gated exception?

## The core idea (v0)

A minimal recurrent state `z_t` that:

1. Evolves continuously even when external input is zero.
2. Can generate its own imagined sensory predictions.
3. Has a gate `g` that turns external prediction error up or down, moving the system between **awake** (g≈1), **daydream** (0<g<1), and **dream** (g≈0) regimes.

Dreams are free rollouts of the dynamics. Daydreams are controlled rollouts loosely coupled to residual sensory error. Subjective continuity is the latent trajectory itself — it never fully resets, it only evolves.

See `prototype/dream_core.py` for a runnable skeleton and `docs/manifesto.md` for the longer-form thesis.

## Status

Early. This is a research notebook that happens to be public. Expect rough edges, half-baked ideas, and honest uncertainty. Feedback, criticism, and collaboration are very welcome — open an issue or start a discussion.

## Related reading

- Hafner et al., *DreamerV3* (Nature, 2025) and *Dreamer 4* (2025) — latent imagination at scale.
- Li et al., *Koopman Dreamer* (arXiv 2607.19719, 2026) — spectrally constrained dynamics for stable long rollouts.
- Motomura (2025), *Dreams... from the Perspective of Predictive Processing* — dreaming as offline generative-model training.
- Tsukuba (2025), REM reactivation of adult-born neurons locking memories in place.
- Konkoly et al. (2026), targeted dream engineering for creative problem-solving.

## License

MIT — use it, fork it, break it, tell us what you find.
