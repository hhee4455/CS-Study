"""
그래프 (Graph) 구현 예제
- 정점(Vertex)들과 간선(Edge)들의 집합
- 방향 그래프(Directed)와 무방향 그래프(Undirected)가 있다
"""

class Graph:
    def __init__(self):
        """
        그래프 초기화
        - 인접 리스트 방식 사용
        """
        self.adjacency_list = {}  # 각 정점에 연결된 이웃들을 저장하는 딕셔너리

    def add_vertex(self, vertex):
        """
        정점 추가 - O(1)
        :param vertex: 추가할 정점
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, directed=False):
        """
        간선 추가 - O(1)
        :param vertex1: 시작 정점
        :param vertex2: 끝 정점
        :param directed: 방향 그래프인지 여부 (False면 무방향 그래프)
        """
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)

        self.adjacency_list[vertex1].append(vertex2)
        if not directed:
            self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2, directed=False):
        """
        간선 삭제 - O(1)
        :param vertex1: 시작 정점
        :param vertex2: 끝 정점
        :param directed: 방향 그래프인지 여부
        """
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].remove(vertex2)
        if not directed:
            if vertex2 in self.adjacency_list and vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        """
        정점 삭제 - O(V+E)
        :param vertex: 삭제할 정점
        """
        if vertex in self.adjacency_list:
            for neighbor in self.adjacency_list[vertex]:
                self.adjacency_list[neighbor].remove(vertex)
            del self.adjacency_list[vertex]

    def __str__(self):
        """
        그래프 출력 (인접 리스트 형식)
        """
        result = ""
        for vertex, neighbors in self.adjacency_list.items():
            result += f"{vertex} -> {neighbors}\n"
        return result