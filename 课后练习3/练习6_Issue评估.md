# 练习6：评估开源项目中的 Issue 质量

## 选取的 Issue

**项目：** Pandas (https://github.com/pandas-dev/pandas)

**Issue 编号：** #54430

**标题：** `read_csv with skipfooter and comment raises ValueError`

## Issue 原文
Environment:

Pandas version: 2.0.3

Python version: 3.11

OS: Ubuntu 22.04

Reproduction:
import pandas as pd
from io import StringIO

data = "# comment\ncol1,col2\n1,2\n3,4\n# footer comment"
pd.read_csv(StringIO(data), comment='#', skipfooter=1, engine='python')

Expected: Should return DataFrame with rows 1,2 and 3,4
Actual: Raises ValueError: "skipfooter not supported with comment"


## 评估

| 标准 | 评估 |
|------|------|
| 尊重维护者时间 | ✅ 提供了完整复现代码和环境信息 |
| 包含必要信息 | ✅ 有版本、OS、错误日志 |
| 复现简单 | ✅ 3行代码即可复现 |
| 期望vs实际清晰 | ✅ 明确说明 |
| 可操作性强 | ✅ 直接指出冲突点 |

**综合评分：** 95/100（优秀 Issue）

## 差的 Issue 示例

标题：read_csv broken
正文：The code doesn't work. Please fix it. This is urgent!!!!


**差在哪：** 没有环境信息、没有复现代码、没有错误日志、语气急躁

## 学习收获

写 Issue 应该：
1. 复现代码必须完整且最小化
2. 环境信息必须完整（OS、版本）
3. 期望 vs 实际分开写清楚
4. 保持专业态度，不抱怨
