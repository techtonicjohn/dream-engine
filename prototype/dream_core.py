"""
dream_core.py
------------
A minimal, runnable skeleton of the Dream Engine idea.

One recurrent latent state z_t that:
  1. evolves even when external input is zero,
  2. can generate its own imagined observations,
  3. has a gate g in [0, 1] that blends external prediction error
     with free imagination — the three regimes (awake / daydream / dream).

This is deliberately tiny: a linear-Gaussian latent dynamics with a
learned-ish transition, an observation model, and a simple error gate.
The point is the *regime logic*, not benchmark performance. Replace the
linear bits with an RSSM / transformer / neural-ODE core whenever you like.

Run:  python prototype/dream_core.py
"""
from __future__ import annotations

import numpy as np


class DreamCore:
    """Continuous latent world model with a dreaming gate."""

    def __init__(
        self,
        dim: int = 16,
        obs_dim: int = 8,
        dt: float = 0.05,
        seed: int = 0,
    ):
        rng = np.random.default_rng(seed)
        self.dim = dim
        self.obs_dim = obs_dim
        self.dt = dt
        # Transition: z <- A z + noise  (replace A with a nonlinear net later)
        self.A = np.eye(dim) + 0.1 * rng.standard_normal((dim, dim)) * dt
        self.A *= 0.98  # mild damping so free rollouts don't explode
        self.C = rng.standard_normal((obs_dim, dim)) * 0.3  # observation model
        self.Q = 0.01 * np.eye(dim)   # process noise (the "spark" of imagination)
        self.R = 0.05 * np.eye(obs_dim)  # observation noise
        self.z = rng.standard_normal(dim) * 0.1
        self.history: list[np.ndarray] = []

    # --- the three regimes, one mechanism ---
    def step(self, obs: np.ndarray | None, g: float) -> dict:
        """Advance one tick.

        g : float in [0, 1]
            1.0 -> awake (fully driven by real sensory error)
            0.5 -> daydream (half imagination, half input)
            0.0 -> dream (pure free rollout, sensors ignored)
        """
        g = float(np.clip(g, 0.0, 1.0))
        # 1. free imagination step (always runs)
        z_imag = self.A @ self.z + np.random.default_rng().standard_normal(self.dim) * np.sqrt(self.Q.diagonal())
        # 2. if there is real input, compute a correction from prediction error
        if obs is not None and g > 0:
            pred = self.C @ self.z
            err = obs - pred
            # simple Kalman-ish gain, scaled by the gate
            K = g * 0.2
            z_corr = self.z + K * (self.C.T @ err)
            self.z = (1 - g) * z_imag + g * z_corr
        else:
            self.z = z_imag  # pure dream
        self.history.append(self.z.copy())
        return {
            "z": self.z.copy(),
            "imagined_obs": self.C @ self.z,
            "regime": "awake" if g > 0.8 else ("daydream" if g > 0.2 else "dream"),
            "gate": g,
        }

    def dream(self, n_steps: int = 50) -> list[np.ndarray]:
        """Close the gate and let the model run free."""
        return [self.step(None, g=0.0)["imagined_obs"] for _ in range(n_steps)]


def demo():
    core = DreamCore(dim=12, obs_dim=6, seed=7)
    print("t | regime   | gate | ||z|| | sample imagined obs")
    for t in range(8):
        obs = np.sin(t * 0.3) * np.ones(6)  # a gentle external signal
        g = 1.0 if t < 3 else (0.4 if t < 6 else 0.0)  # awake -> daydream -> dream
        out = core.step(obs, g)
        print(f"{t} | {out['regime']:8} | {out['gate']:.1f}  | {np.linalg.norm(out['z']):.2f} | "
              f"{np.round(out['imagined_obs'][:3], 2)}")
    print("\n--- pure dream rollout (gate closed) ---")
    dream_traj = core.dream(6)
    for i, d in enumerate(dream_traj):
        print(f"dream step {i}: {np.round(d[:3], 2)}")


if __name__ == "__main__":
    demo()
