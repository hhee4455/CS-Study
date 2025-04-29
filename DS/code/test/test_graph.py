import pytest
import sys
import os

# 모듈 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DS_06_graph import Graph


# ---------------------------
# 정상 동작 테스트
# ---------------------------

def test_add_vertex():
    graph = Graph()
    graph.add_vertex("A")

    assert "A" in graph.adjacency_list
    assert graph.adjacency_list["A"] == []

def test_add_edge_undirected():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B")

    assert "B" in graph.adjacency_list["A"]
    assert "A" in graph.adjacency_list["B"]

def test_add_edge_directed():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B", directed=True)

    assert "B" in graph.adjacency_list["A"]
    assert "A" not in graph.adjacency_list["B"]

def test_add_edge_auto_create_vertices():
    graph = Graph()
    graph.add_edge("A", "B")  # 정점이 없었지만 자동 추가됨

    assert "A" in graph.adjacency_list
    assert "B" in graph.adjacency_list
    assert "B" in graph.adjacency_list["A"]
    assert "A" in graph.adjacency_list["B"]


# ---------------------------
# 삭제 동작 테스트
# ---------------------------

def test_remove_edge_undirected():
    graph = Graph()
    graph.add_edge("A", "B")
    graph.remove_edge("A", "B")

    assert "B" not in graph.adjacency_list["A"]
    assert "A" not in graph.adjacency_list["B"]

def test_remove_edge_directed():
    graph = Graph()
    graph.add_edge("A", "B", directed=True)
    graph.remove_edge("A", "B", directed=True)

    assert "B" not in graph.adjacency_list["A"]
    assert "A" not in graph.adjacency_list["B"]

def test_remove_vertex():
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.remove_vertex("A")

    assert "A" not in graph.adjacency_list
    assert "A" not in graph.adjacency_list["B"]
    assert "A" not in graph.adjacency_list["C"]


# ---------------------------
# 출력 테스트
# ---------------------------

def test_graph_structure_output():
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")

    output = str(graph)
    assert "A -> ['B', 'C']" in output or "A -> ['C', 'B']" in output
    assert "B -> ['A']" in output
    assert "C -> ['A']" in output
