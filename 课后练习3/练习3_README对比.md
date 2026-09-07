# 练习3：对比 3 个 GitHub 项目的 README

## 1. VSCode (https://github.com/microsoft/vscode)

- **第一屏展示什么？** 大量徽章（build status, license, downloads, twitter等）+ 截图（代码编辑界面）+ 一句话说明“VS Code is a source code editor”。
- **安装步骤清晰吗？** 比较清晰。有 Windows/Linux/macOS 三种平台的下载按钮和安装说明。
- **最有用部分：** 截图直观展示了编辑器界面，下载按钮位置明显。
- **噪音部分：** 徽章太多（超过10个），普通用户根本看不懂大部分徽章的含义。

## 2. PyTorch (https://github.com/pytorch/pytorch)

- **第一屏展示什么？** 大量徽章 + 一句“Tensors and Dynamic neural networks in Python” + 两行代码示例。
- **有没有代码示例？** 有。开头就是 `import torch` 和 `torch.tensor` 的简单示例，一看就懂。
- **最有用部分：** 代码示例让人立刻知道这个库是干什么的，文档和教程链接也很清晰。
- **噪音部分：** 徽章同样很多，安装命令表格很长，对新手不友好。

## 3. Ruff (https://github.com/astral-sh/ruff)

- **第一屏展示什么？** 一句“An extremely fast Python linter and code formatter” + 性能对比图表（速度秒杀其他工具）+ 简单的安装命令 `pip install ruff`。
- **和 VSCode/PyTorch 比风格不同在哪？** 非常简洁，没有任何多余的徽章，一屏之内说清楚“这是什么”“多快”“怎么装”，直接进入主题。
- **最有用部分：** 性能对比图表最有说服力，让人立刻相信它很快。
- **噪音部分：** 几乎没有废话，唯一可能算噪音的是性能对比的详细数字表格，对普通用户略多。

## 总结

三个 README 都优秀，但风格不同：

- **VSCode**：全面型，适合大型项目
- **PyTorch**：教程型，适合框架类项目  
- **Ruff**：极简型，适合工具类项目

以后我写 README 会模仿 **Ruff** 的风格：先说明“这是什么”，再用一两个示例展示“怎么用”，避免过多徽章和冗余信息。
