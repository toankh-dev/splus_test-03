import pytest

from target import TempModule  # テスト対象のクラスをインポート

# TC1: 正常系：runメソッドを引数なしで呼び出した場合、"temp"が返ることを確認する
def test_run_returns_temp_TC1():
    # インスタンスを生成
    temp_module = TempModule()
    # runメソッドを呼び出し、戻り値を検証
    assert temp_module.run() == "temp"
```
