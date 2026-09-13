import argparse
import sys


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True)
    a = p.parse_args()

    # 检查 name 是否只包含空白字符
    if not a.name or a.name.isspace():
        print("Error: name cannot be empty or whitespace only", file=sys.stderr)
        sys.exit(2)

    print(f"Hello, {a.name}!")
