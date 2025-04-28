"""
큐 (Queue) 구현 예제
- 선입선출(FIFO) 구조
- 데이터를 한 쪽 끝에서 추가하고, 반대쪽 끝에서 제거한다.
"""

class Queue:
    def __init__(self, capacity):
        """
        고정된 크기의 큐 생성
        :param capacity: 큐의 최대 크기
        """
        self.capacity = capacity
        self.data = [None] * capacity # 큐 저장 공간 초기화
        self.front = 0 # 첫 번째 요소 인덱스
        self.rear = 0 # 마지막 요소 다음 인덱스
        self.size = 0 # 현재 요소 개수

    def enqueue(self, value):
        """
        큐의 값 추가 (enqueue) - O(1)
        :param value: 추가할 값
        """
        if self.size >= self.capacity:
            raise OverflowError("큐가 가득 찼습니다. 더 이상 추가할 수 없습니다.")
        
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        """
        큐에서 값 제거 (dequeue) - O(1)
        :return: 제거된 값
        """
        if self.is_empty():
            raise IndexError("큐가 비어 있습니다. 삭제할 수 없습니다.")
        
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value
    
    def peek(self):
        """
        큐의 맨 앞 조회 - O(1)
        :return: 맨 앞 값
        """
        if self.is_empty():
            raise IndexError("큐가 비어 있습니다. 조회할 수 없습니다.")
        
        return self.data[self.front]
    
    def is_empty(self):
        """
        큐가 비어 있는지 확인 - O(1)
        :return: True/False
        """

        return self.size == 0
    
    def __str__(self):
        """
        큐 출력 (현재 삽입된 요소만)
        """
        result = []
        idx = self.front
        for _ in range(self.size):
            result.append(self.data[idx])
            idx = (idx + 1) % self.capacity
        return str(result)