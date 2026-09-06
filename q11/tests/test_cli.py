import pytest
from greetlab.cli import main

def test_blank_name_exits_with_error():
    """当 name 只含空白字符时，应该以 SystemExit(2) 退出"""
    with pytest.raises(SystemExit) as exc_info:
        # 模拟命令行参数 --name " "
        import sys
        sys.argv = ["cli.py", "--name", " "]
        main()
    assert exc_info.value.code == 2
