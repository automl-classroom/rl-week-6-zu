import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from rliable import library as rly
from rliable import metrics, plot_utils

baselines = ["none", "avg", "value", "gae"]
score_dict = {}

for name in baselines:
    df = pd.read_csv(f"{name}.csv", names=["step", "mean", "std"])
    scores = np.array(df["mean"].tolist())
    score_dict[name] = [scores]  # 必须包成 list of np.array

# 定义多个聚合指标
aggregate_fns = {
    "Mean": metrics.aggregate_mean,
    "IQM": metrics.aggregate_iqm,
    "Median": metrics.aggregate_median,
    "Optimality Gap": metrics.aggregate_optimality_gap,
}

# 计算聚合指标 + CI
aggregate_scores, aggregate_cis = rly.get_interval_estimates(
    score_dict, aggregate_fns, reps=5000
)

# 绘图并保存
fig, ax = plot_utils.plot_interval_estimates(
    aggregate_scores,
    aggregate_cis,
    metric_names=list(aggregate_fns.keys()),
    algorithms=baselines,
    xlabel="Aggregate Metrics",
)
plt.suptitle("Actor-Critic Baseline Comparison (RLiable)", fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("baseline_comparison_metrics.png", dpi=300)
plt.savefig("baseline_comparison_metrics.pdf")
plt.show()
