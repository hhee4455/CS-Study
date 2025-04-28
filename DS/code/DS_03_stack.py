"""
스택 (Stack) 구현 예제
- 후입선출(LIFO) 구조
- 데이터를 한 쪽 끝에서만 삽입과 삭제 가능
"""

class Stack:
    def __init__(self, capacity):
        """
        고정된 크기의 스택 생성
        :param capacity: 스택의 최대 크기
        """
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def push(self, value):
        """
        스택에 값 추가 (push) - O(1)
        :param value: 추가할 값
        """
        if self.size >= self.capacity:
            raise OverflowError("스택이 가득 찼습니다. 더 이상 추가할 수 없습니다.")
        
        self.data[self.size] = value
        self.size += 1

    def pop(self):
        """
        스택에서 값 제거 (pop) - O(1)
        :return: 제거된 값
        """
        if self.is_empty():
            raise IndexError("스택이 비어 있습니다. 삭제할 수 업습니다.")

        value = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return value

    def peek(self):
        """
        스택의 맨 위 값 조회 - O(1)
        :return: 맨 위 값
        """
        if self.is_empty():
            raise IndexError("스택이 비어 있습니다. 조회할 수 없습니다.")
        
        return self.data[self.size - 1]
    
    def is_empty(self):
        """
        스택이 비어 있는지 확인 - O(1)
        :return: True/False
        """
        return self.size == 0
    
    def __str__(self):
        """
        스택 출력 (현재 삽입된 요소만)
        """
        return str([self.data[i] for i in range(self.size)])