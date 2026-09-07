# 练习7：创建 Python 包并生成 Lockfile

## 操作步骤

1. 激活虚拟环境：`source ../venv_clean/bin/activate`
2. 生成 lockfile：`pip freeze > requirements_lock.txt`
3. 查看内容：`cat requirements_lock.txt`

## 生成的 lockfile 内容
exceptiongroup==1.3.1
greetlab-25020007173==0.1.0
iniconfig==2.3.0
packaging==26.3
pluggy==1.6.0
pytest==9.1.1
tomli==2.4.1
typing_extensions==4.16.0


## 解释

| 文件 | 作用 | 版本约束 |
|------|------|----------|
| `pyproject.toml` | 声明依赖 | 宽松（如 `>=68`） |
| `requirements_lock.txt` | 锁定精确版本 | 严格（如 `==68.2.2`） |

锁文件保证团队成员安装的依赖版本完全一致。
