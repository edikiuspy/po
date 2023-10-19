from io import StringIO

from _pytest.capture import CaptureFixture

from sito.main import main
import pytest
from _pytest.monkeypatch import MonkeyPatch
@pytest.fixture
def test_exists_main_function(monkeypatch:MonkeyPatch) -> None:
    main(1)
def test_returns_correct_result(monkeypatch:MonkeyPatch ,capsys: CaptureFixture) -> None:
    monkeypatch.setattr('sys.stdin', StringIO('20'))
    i=int(input())
    assert main(i)==[2, 3, 5, 7,11,13,17,19]
def test_min_input(monkeypatch:MonkeyPatch) -> None:
    with pytest.raises(Exception) as e:
        monkeypatch.setattr('sys.stdin', StringIO('0'))
        main(int(input()))
        assert "Number can't be lower than 1" in str(e.value)
def test_small_input(monkeypatch:MonkeyPatch) -> None:
    monkeypatch.setattr('sys.stdin', StringIO('1'))
    assert main(int(input())) == []
def test_large_input(monkeypatch:MonkeyPatch) -> None:
    monkeypatch.setattr('sys.stdin', StringIO('50'))
    assert main(int(input()))==[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
def test_negative_input(monkeypatch:MonkeyPatch) -> None:
    with pytest.raises(Exception) as e:
        monkeypatch.setattr('sys.stdin', StringIO('-10'))
        main(int(input()))
        assert "Number can't be lower than 1" in str(e.value)
def test_float_input(monkeypatch:MonkeyPatch) -> None:
    monkeypatch.setattr('sys.stdin', StringIO('10.5'))
    assert main(float(input()))==[2,3,5,7]