# Issue: sdt-greet 在 Windows 上处理空格参数时行为异常

## 环境
- 操作系统：Windows 10/11（待确认具体版本）
- 工具版本：sdt-greet 0.1.0

## 复现命令
sdt-greet --name " "

## 期望结果
程序应输出错误信息并以非零退出码（2）结束

## 实际结果
程序输出 "Hello, !" 并以 0 退出

## 补充信息
- 其他参数（如 --name "abc"）工作正常
- Linux 环境下的行为待确认

---

# Commit Message

fix: 处理 --name 参数为空白字符时未正确退出

问题：
当用户传入只包含空白字符的 --name 参数（如 " "）时，程序仍输出 "Hello, !" 并以 0 退出，导致用户误以为操作成功。

解决方案：
在 main() 函数中增加空白字符检查，当 name 为 None 或仅包含空白字符时，输出错误信息到 stderr 并以 SystemExit(2) 退出。

影响范围：
仅修改 cli.py，不影响其他功能。

---

# Code Review Comment

**类型：Blocking**

**位置**：src/greetlab/cli.py

**具体问题**：
当前代码在接收到空白字符参数（如 --name " "）时，仍输出 "Hello, !" 并以 0 退出，没有校验用户输入的有效性。

**风险**：
脚本可能在自动化流程中被误用，导致下游任务依赖错误结果继续执行。

**建议修改**：
在打印问候语前增加参数校验，对空白字符串抛出 SystemExit(2)。

**参考实现**：
if not a.name or a.name.isspace():
    print("Error: name cannot be empty or whitespace only", file=sys.stderr)
    sys.exit(2)
