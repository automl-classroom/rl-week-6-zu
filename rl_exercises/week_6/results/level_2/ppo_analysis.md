# PPO vs ActorCritic Analysis

## Experiment Setup

We compare three agents on the `LunarLander-v3` environment:

- **PPO (vanilla)**: Standard PPO implementation with fixed learning rate.
- **PPO + Enhancements**: Includes KL early stopping and linear learning rate decay.
- **ActorCritic**: Baseline implementation from Level 1 using REINFORCE with GAE/value/avg baselines.

Each model was trained for 20,000 steps and evaluated every 10,000 steps.

---

## Observations

- **PPO (vanilla)** showed an initial strong return around -127.78 but degraded to -205.87 in later training.
- **PPO + Enhancements** started similarly, but stabilized better in the second half and maintained stronger return.
- **ActorCritic** underperformed both PPO variants across all steps.

---

## Analysis

- **Enhancements Effectiveness**: KL early stopping likely prevented over-updating, while learning rate decay contributed to stabilization in later training stages.
- **PPO vs ActorCritic**: PPO uses clipped surrogate objectives and more robust training heuristics, leading to higher and more stable returns.
- **Return Volatility**: ActorCritic returns were lower and more volatile, consistent with high-variance policy gradient behavior.

---

## Conclusion

>  **PPO with enhancements** delivered the best trade-off between stability and performance in limited steps.  
>  **ActorCritic** may benefit from longer training or stronger baselines.