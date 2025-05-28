#!/bin/bash

# 确保 results 文件夹存在
mkdir -p results

# 循环四种 baseline
for BASELINE in none avg value gae
do
  echo "Running baseline: $BASELINE"

  # 运行训练脚本（注意路径）
  python rl_exercises/week_6/actor_critic.py \
    agent.baseline_type=$BASELINE \
    train.total_steps=100000 \
    train.eval_interval=5000 \
    train.eval_episodes=5 \
    hydra.run.dir=results/$BASELINE
done
