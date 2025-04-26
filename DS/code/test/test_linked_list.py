import pytest
import sys
import os

# 모듈 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DS_02_linked_list import LinkedList


# ---------------------------
# 정상 동작 테스트
# ---------------------------

def test_insert_multiple_values():
    ll = LinkedList()
    ll.insert(0, 10)
    ll.insert(1, 20)
    ll.insert(1, 15)

    assert ll.get(0) == 10
    assert ll.get(1) == 15
    assert ll.get(2) == 20
    assert ll.size == 3

def test_delete_middle_element():
    ll = LinkedList()
    ll.insert(0, "a")
    ll.insert(1, "b")
    ll.insert(2, "c")
    ll.delete(1)

    assert ll.get(0) == "a"
    assert ll.get(1) == "c"
    assert ll.size == 2

def test_get_value():
    ll = LinkedList()
    ll.insert(0, "first")
    ll.insert(1, "second")

    assert ll.get(0) == "first"
    assert ll.get(1) == "second"

def test_find_existing_value():
    ll = LinkedList()
    ll.insert(0, "apple")
    ll.insert(1, "banana")
    ll.insert(2, "cherry")

    assert ll.find("apple") == 0
    assert ll.find("banana") == 1
    assert ll.find("cherry") == 2

def test_find_non_existing_value():
    ll = LinkedList()
    ll.insert(0, "apple")
    ll.insert(1, "banana")

    assert ll.find("orange") == -1  # 존재하지 않는 값 검색


# ---------------------------
# 예외 상황 테스트
# ---------------------------

@pytest.mark.parametrize("index", [-1, 1])
def test_insert_invalid_index(index):
    ll = LinkedList()
    with pytest.raises(IndexError, match="삽입 인덱스가 유효하지 않습니다"):
        ll.insert(index, "error")

@pytest.mark.parametrize("index", [-1, 0, 1])
def test_delete_invalid_index(index):
    ll = LinkedList()
    with pytest.raises(IndexError, match="삭제 인덱스가 유효하지 않습니다"):
        ll.delete(index)

@pytest.mark.parametrize("index", [-1, 0, 1])
def test_get_invalid_index(index):
    ll = LinkedList()
    with pytest.raises(IndexError, match="조회 인덱스가 유효하지 않습니다"):
        ll.get(index)


# ---------------------------
# 문자열 출력 테스트
# ---------------------------

def test_str_output():
    ll = LinkedList()
    ll.insert(0, 1)
    ll.insert(1, 2)
    ll.insert(2, 3)

    assert str(ll) == "[1, 2, 3]"
