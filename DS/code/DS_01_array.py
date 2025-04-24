"""
배열 (Array) 구현 예제
- 고정된 크기의 배열을 가정하여 구현
- 인덱스를 기반으로 빠른 접근이 가능
- 중간 삽입/삭제 시 전체 데이터를 이동해야 하므로 느림
"""

class Array:
    def __init__(self, capacity):
        """
        고정된 크기의 배열 생성
        :param capacity: 배열의 최대 크기
        """
        self.capacity = capacity
        self.data = [None] * capacity  # 배열 초기화
        self.size = 0 # 현재 요소 개수

    def insert(self, index, value):
        """
        지정한 위치에 값 삽입 - O(n)
        :param index: 삽입할 위치
        :param value: 삽입할 값
        """
        if self.size >= self.capacity:
            raise OverflowError("배열이 가득 찼습니다. 더 이상 삽입할 수 없습니다.")
        
        if index < 0 or index > self.size:
            raise IndexError("삽입 인덱스가 유효하지 않습니다")

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1

    def delete(self, index):
        """
        지정한 위치의 값 삭제 - O(n)
        :param index: 삭제할 위치
        """
        if index < 0 or index >= self.size:
            raise IndexError("삭제 인덱스가 유효하지 않습니다")
        
        # 뒤에 요소들을 한 칸씩 앞으로 이동
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.size -= 1
        self.data[self.size] = None


    def get(self, index):
        """
        특정 위치의 값 조회 - O(1)
        :param index: 조회할 위치
        """
        if index < 0 or index >= self.size:
            raise IndexError("조회 인덱스가 유효하지 않습니다")
        
        return self.data[index]

    def __str__(self):
        """
        배열 출력 (현재 삽입된 요소만)
        """
        return str([self.data[i] for i in range(self.size)])