"""
연결 리스트(LinkedList) 구현 예제
- 선형적으로 데이터를 연결하여 저장
- 삽입/삭제가 빠르다 (O(1) 또는 O(n))
- 임의 접근이 느리다 (O(n))
"""

class Node:
    """
    노드 (Node) 클래스
    - 데이터와 다음 노드를 저장한다
    """
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        """
        연결 리스트 생성
        """
        self.head = None
        self.size = 0 # 현재 요소 개수

    def insert(self, index, value):
        """
        지정한 위치에 값 삽입 - O(n)
        :param index: 삽입할 위치
        :param value: 삽입할 값 
        """
        if index < 0 or index > self.size:
            raise IndexError("삽입 인덱스가 유효하지 않습니다.")
        
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
        
        self.size += 1
    
    def delete(self, index):
        """
        지정한 위치의 값 삭제 - O(n)
        :param index: 삭제할 위치
        """
        if index < 0 or index >= self.size:
            raise IndexError("삭제 인덱스가 유효하지 않습니다.")

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            
            current.next = current.next.next

        self.size -= 1
    
    def get(self, index):
        """
        특정 위치의 값 조회 - O(n)
        :param index: 조회할 위치
        """
        if index < 0 or index >= self.size:
            raise IndexError("조회 인덱스가 유효하지 않습니다.")
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.data
    
    def find(self, value):
        """
        주어진 값을 처음 찾은 인덱스를 반환 - O(n)
        :param value: 찾을 값
        :return: 찾으면 인덱스, 없으면 -1
        """
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def __str__(self):
        """
        연결 리스트 출력(현재 삽입된 요소만)
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return str(result)