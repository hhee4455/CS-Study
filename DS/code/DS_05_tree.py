"""
트리 (Tree) 구현 예제
- 계층적 구조를 가진 자료구조
- 하나의 루트 노드 기준으로 여러 자식 노드가 연결된다.
"""

class TreeNode:
    """
    트리 노드 클래스
    - 데이터와 자식 노드들을 저장한다.
    """
    def __init__(self, value):
        self.value = value
        self.children = [] # 여러 자식을 가질 수 있음

    def add_child(self, child_node):
        """
        현재 노드에 자식 노드를 추가한다. - O(1)
        :param child_node: 추가할 자식 노드 (TreeNode)
        """
        self.children.append(child_node)

    def remove_child(self, child_node):
        """
        현재 노드에서 특정 자식 노드를 제거한다 - O(n)
        :param child_node: 제거할 자식 노드 (TreeNode)
        """
        if child_node in self.children:
            self.children.remove(child_node)

    def __str__(self):
        """
        현재 노드 및 하위 트리를 문자열로 표현한다 (DFS 기반) - O(n)
        """
        return self._build_str()

    def _build_str(self, level=0):
        """
        내부 메서드: 트리를 문자열로 재귀적으로 구성
        """
        result = " " * (level * 2) + f"{self.value}\n"
        for child in self.children:
            result += child._build_str(level + 1)
        return result