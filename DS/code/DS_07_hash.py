"""
해시 테이블 (Hash Table) 구현 예제
- 키(Key)를 해시 함수(Hash Function)를 통해 고유한 인덱스로 변환하여 저장
- 빠른 조회(O(1)), 삽입(O(1)), 삭제(O(1)) 가능
- 충돌(해시 충돌, Collision) 발생 시 체이닝(Chaining) 방식으로 해결
"""

class HashTable:
    def __init__(self, capacity=10):
        """
        고정된 크기의 해시 테이블 생성
        :param capacity: 테이블의 크기
        """
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]  # 체이닝을 위한 리스트의 리스트
        self.size = 0  # 저장된 데이터 수

    def _hash(self, key):
        """
        내부 해시 함수
        :param key: 키 값
        :return: 테이블 인덱스
        """
        return hash(key) % self.capacity

    def insert(self, key, value):
        """
        키-값 쌍 삽입 - O(1) (평균)
        :param key: 키
        :param value: 값
        """
        index = self._hash(key)

        # 키가 이미 존재하는 경우 업데이트
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return

        # 존재하지 않으면 새로 추가
        self.table[index].append((key, value))
        self.size += 1

    def get(self, key):
        """
        키로 값 조회 - O(1) (평균)
        :param key: 조회할 키
        :return: 값
        """
        index = self._hash(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        raise KeyError("키를 찾을 수 없습니다")

    def delete(self, key):
        """
        키-값 쌍 삭제 - O(1) (평균)
        :param key: 삭제할 키
        """
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.size -= 1
                return

        raise KeyError("삭제할 키를 찾을 수 없습니다")

    def __str__(self):
        """
        현재 해시 테이블 출력
        """
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                result.append(f"{i}: {bucket}")
        return "\n".join(result)
