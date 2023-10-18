from sito.main import main
import pytest
@pytest.fixture
def values() -> list[int]:
    return [20,0,1,50,-10,10.5]
def test_exists_main_function(values: list[int]) -> None:
    main(1)
def test_returns_correct_result(values:list[int]) -> None:
    result = main(values[0])
    assert result==[2, 3, 5, 7,11,13,17,19]
def test_min_input(values:list[int]) -> None:
    with pytest.raises(Exception) as e:
        main(values[1])
        assert "Number can't be lower than 1" in str(e.value)
def test_small_input(values:list[int]) -> None:
    result = main(values[2])
    assert result == []
def test_large_input(values:list[int]) -> None:
    result = main(values[3])
    assert result==[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
def test_negative_input(values:list[int]) -> None:
    with pytest.raises(Exception) as e:
        main(values[4])
        assert "Number can't be lower than 1" in str(e.value)
def test_float_input(values:list[int]) -> None:
    with pytest.raises(Exception) as e:
        main(values[5])
        assert "Number can't be lower than 1" in str(e.value)