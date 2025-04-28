import pytest
import sys
import os

# 모듈 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DS_04_queue import Queue


# ---------------------------
# 정상 동작 테스트
# ---------------------------

def test_enqueue_multiple_values():
    queue = Queue(5)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    assert queue.peek() == 10
    assert str(queue) == "[10, 20, 30]"
    assert queue.size == 3

def test_dequeue_value():
    queue = Queue(5)
    queue.enqueue(1)
    queue.enqueue(2)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.is_empty() == True

def test_peek_value():
    queue = Queue(5)
    queue.enqueue(100)

    assert queue.peek() == 100
    assert not queue.is_empty()

def test_is_empty_on_new_queue():
    queue = Queue(3)
    assert queue.is_empty() == True


# ---------------------------
# 예외 상황 테스트
# ---------------------------

def test_enqueue_overflow():
    queue = Queue(2)
    queue.enqueue(1)
    queue.enqueue(2)
    with pytest.raises(OverflowError, match="큐가 가득 찼습니다"):
        queue.enqueue(3)

def test_dequeue_underflow():
    queue = Queue(2)
    with pytest.raises(IndexError, match="큐가 비어 있습니다"):
        queue.dequeue()

def test_peek_empty_queue():
    queue = Queue(2)
    with pytest.raises(IndexError, match="큐가 비어 있습니다"):
        queue.peek()
