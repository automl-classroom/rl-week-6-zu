# Actor-Critic Baseline Analysis

## 1. Do some baselines learn faster or reach higher returns?

Based on the evaluation curves:

- **None** and **avg** baselines exhibit slightly more stable and improving performance in the later stages.
- **Value** and **GAE** baselines show large fluctuations and eventually decline, suggesting instability or poor learning under current settings.
- No baseline consistently reaches significantly higher return, but `avg` shows marginally better long-term stability.

## 2. Conceptual Justification for Observed Differences

- **None (no baseline):** High variance in return estimates leads to unstable updates, but can perform reasonably well in simple environments.

- **Avg (running average):** Reduces variance by subtracting a global average, though it's slower to adapt. Explains why it's more stable and less noisy.

- **Value (critic):** Estimates value function per state, but introduces potential bias if the critic is under-trained. This explains the high fluctuation.

- **GAE (Generalized Advantage Estimation):** In theory offers best bias-variance tradeoff. However, if the value network is inaccurate, it can cause unstable advantages — seen in the sharp swings and decline in return.

## 3. Recommendation

For this assignment and settings:

- `avg` baseline is the most reliable and interpretable.
- `value` and `gae` need further tuning of the critic to show advantages.

---

*Note: Results may vary with different learning rates, hidden sizes, or environments. GAE is often better in continuous control tasks like MuJoCo.*