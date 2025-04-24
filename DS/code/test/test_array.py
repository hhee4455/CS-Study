import pytest
import sys
import os

# 모듈 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DS_01_array import Array

# ---------------------------
# 정상 동작 테스트
# ---------------------------

def test_insert_multiple_values():
    arr = Array(5)
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(1, 15)

    assert arr.get(0) == 10
    assert arr.get(1) == 15
    assert arr.get(2) == 20
    assert arr.size == 3

def test_delete_middle_element():
    arr = Array(3)
    arr.insert(0, "a")
    arr.insert(1, "b")
    arr.insert(2, "c")
    arr.delete(1)

    assert arr.get(0) == "a"
    assert arr.get(1) == "c"
    assert arr.size == 2

# ---------------------------
# 예외 상황 테스트
# ---------------------------

@pytest.mark.parametrize("index", [-1, 5])
def test_insert_invalid_index(index):
    arr = Array(3)
    with pytest.raises(IndexError, match="삽입 인덱스가 유효하지 않습니다"):
        arr.insert(index, 99)

def test_insert_overflow():
    arr = Array(2)
    arr.insert(0, 1)
    arr.insert(1, 2)
    with pytest.raises(OverflowError, match="배열이 가득 찼습니다"):
        arr.insert(2, 3)

@pytest.mark.parametrize("index", [-1, 1])
def test_delete_invalid_index(index):
    arr = Array(1)
    arr.insert(0, 10)
    arr.delete(0)  # 삭제 후 빈 상태
    with pytest.raises(IndexError, match="삭제 인덱스가 유효하지 않습니다"):
        arr.delete(index)

def test_get_invalid_index():
    arr = Array(2)
    with pytest.raises(IndexError, match="조회 인덱스가 유효하지 않습니다"):
        arr.get(0)

# ---------------------------
# 문자열 출력 확인
# ---------------------------

def test_str_output():
    arr = Array(3)
    arr.insert(0, 1)
    arr.insert(1, 2)
    assert str(arr) == "[1, 2]"
