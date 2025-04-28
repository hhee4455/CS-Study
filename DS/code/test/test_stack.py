import pytest
import sys
import os

# 모듈 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DS_03_stack import Stack


# ---------------------------
# 정상 동작 테스트
# ---------------------------

def test_push_multiple_values():
    stack = Stack(5)
    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.peek() == 30
    assert str(stack) == "[10, 20, 30]"
    assert stack.size == 3

def test_pop_value():
    stack = Stack(5)
    stack.push(1)
    stack.push(2)

    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty() == True

def test_peek_value():
    stack = Stack(5)
    stack.push(100)

    assert stack.peek() == 100
    assert not stack.is_empty()

def test_is_empty_on_new_stack():
    stack = Stack(3)
    assert stack.is_empty() == True


# ---------------------------
# 예외 상황 테스트
# ---------------------------

def test_push_overflow():
    stack = Stack(2)
    stack.push(1)
    stack.push(2)
    with pytest.raises(OverflowError, match="스택이 가득 찼습니다"):
        stack.push(3)

def test_pop_underflow():
    stack = Stack(2)
    with pytest.raises(IndexError, match="스택이 비어 있습니다"):
        stack.pop()

def test_peek_empty_stack():
    stack = Stack(2)
    with pytest.raises(IndexError, match="스택이 비어 있습니다"):
        stack.peek()
