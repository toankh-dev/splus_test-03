import pytest

from target import TempModule  # テスト対象のクラスをインポート（ファイル名がtarget.pyの場合）

# TC1: 正常系 runメソッドを引数なしで呼び出した場合、常に"temp"が返ることを確認する
def test_TC1_run_returns_temp():
    # インスタンス生成
    temp_module = TempModule()
    # runメソッドを引数なしで呼び出し
    result = temp_module.run()
    # 期待値を検証
    assert result == "temp"

# TC2: 境界値テスト runメソッドは引数を受け付けないため、引数なしで呼び出すケースのみ
def test_TC2_run_no_arguments():
    temp_module = TempModule()
    # 引数なしで呼び出し
    result = temp_module.run()
    assert result == "temp"

# TC3: 異常系 runメソッドは例外を発生しないことを確認する
def test_TC3_run_no_exception():
    temp_module = TempModule()
    # 例外が発生しないことを確認
    try:
        temp_module.run()
    except Exception as e:
        pytest.fail(f"runメソッドで例外が発生しました: {e}")

# TC4: 入力パラメータが空リストや空辞書の場合でもrunメソッドは引数を受け付けないため、無視されることを確認する
@pytest.mark.parametrize(
    "flg, source, method_args",
    [
        ([], {}, []),  # 空リスト, 空辞書, 空リスト
    ]
)
def test_TC4_run_with_empty_list_and_dict(flg, source, method_args):
    temp_module = TempModule()
    # runメソッドは引数を受け付けないため、引数を渡すとTypeErrorになることを確認
    with pytest.raises(TypeError):
        temp_module.run(flg)
    with pytest.raises(TypeError):
        temp_module.run(source)
    with pytest.raises(TypeError):
        temp_module.run(method_args)

# TC5: 入力パラメータに値が設定されていてもrunメソッドは引数を受け付けないため、無視されることを確認する
@pytest.mark.parametrize(
    "flg, source, method_args",
    [
        ([True, False], {"m_1": "test"}, [1, 2, 3]),
    ]
)
def test_TC5_run_with_various_values(flg, source, method_args):
    temp_module = TempModule()
    # runメソッドは引数を受け付けないため、引数を渡すとTypeErrorになることを確認
    with pytest.raises(TypeError):
        temp_module.run(flg)
    with pytest.raises(TypeError):
        temp_module.run(source)
    with pytest.raises(TypeError):
        temp_module.run(method_args)

# TC6: 入力パラメータがNoneの場合でもrunメソッドは引数を受け付けないため、無視されることを確認する
def test_TC6_run_with_none():
    temp_module = TempModule()
    # runメソッドは引数を受け付けないため、Noneを渡すとTypeErrorになることを確認
    with pytest.raises(TypeError):
        temp_module.run(None)

# TC7: 入力パラメータに異なる型の値が設定されていてもrunメソッドは引数を受け付けないため、無視されることを確認する
@pytest.mark.parametrize(
    "flg, source, method_args",
    [
        ([0, 1], {"func": 123}, ["a", "b"]),
    ]
)
def test_TC7_run_with_different_types(flg, source, method_args):
    temp_module = TempModule()
    # runメソッドは引数を受け付けないため、引数を渡すとTypeErrorになることを確認
    with pytest.raises(TypeError):
        temp_module.run(flg)
    with pytest.raises(TypeError):
        temp_module.run(source)
    with pytest.raises(TypeError):
        temp_module.run(method_args)