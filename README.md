# 戚氏弧长算法 (Crishi Arc Length Algorithm)

**一种高效、自适应、高精度的曲线弧长数值计算方法**

**作者：戚华建（原创发明人）**  
**版本：v3.0（终极普适版）**  
**日期：2025年12月**

## 简介

戚氏弧长算法是一种源于工程实践的创新数值方法，通过折线逼近、局部曲率权重校正和全自适应递归细分，实现对任意复杂曲线的快速、高精度弧长计算。

**核心优势**：
- 无需解析求导或复杂积分
- 自动在曲率大处加密采样，平坦处稀疏
- 支持参数曲线、显式函数、离散点三种输入
- 精度可控（误差容限任意设定）
- 计算效率极高（典型案例用数百点达1e-10精度）

适用于工程路径规划、机器人轨迹、计算机图形、物理模拟、测量数据处理等场景。

## 安装

```bash
pip install numpy

## 快速开始

```python
from crishi_arclength import crishi_arclength_v3
import numpy as np

# 示例1：三维螺旋线 r(t) = (cos t, sin t, t/2), t ∈ [0, 2π]
def helix(t):
    return [np.cos(t), np.sin(t), t/2]

L, err, n = crishi_arclength_v3(helix, 0, 2*np.pi, tol=1e-8, mode='parametric')
print(f"弧长: {L:.10f}  估计误差: <{err:.2e}  采样点: {n}")

# 示例2：y = sin(x), x ∈ [0, π]
L, err, n = crishi_arclength_v3(np.sin, 0, np.pi, tol=1e-8, mode='explicit')
print(f"弧长: {L:.10f}")

# 示例3：离散点序列
points = np.array([[0,0], [1,1], [2,0], [3,2]])
L, _, _ = crishi_arclength_v3(points, mode='discrete')
print(f"弧长: {L:.6f}")

```
```python

## 算法起源（早期工程版）

`early_engineering_version.py` 是作者戚华建在工程实践中最早使用的版本，  
专门解决“已知弦高 H 和半弦长 L 求圆弧长”的现场计算问题。  
它简洁高效、无需复杂工具，是整个戚氏弧长算法的起点与灵感来源！
```

```markdown
## 致谢

本算法核心思想由戚华建在工程实践中独立提出。  
文档初稿由 ChatGPT 协助形式整理，算法优化、代码实现、自适应机制完善及终极版开发由 Grok（xAI）深度参与和指导。  
特别感谢 ChatGPT 和 Grok 两位 AI 老师的宝贵帮助！

```
```
## 开源协议

MIT License - 完全免费使用、修改、商用。

欢迎 Star ⭐、Fork、提交 Issue 反馈！  
让我们一起把戚氏弧长算法推广到全世界！

```

