import pytest
import sys
import os

# 모듈 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DS_05_tree import TreeNode


# ---------------------------
# 정상 동작 테스트
# ---------------------------

def test_create_tree_node():
    node = TreeNode("Root")
    assert node.value == "Root"
    assert node.children == []

def test_add_child_node():
    root = TreeNode("Root")
    child = TreeNode("Child")

    root.add_child(child)

    assert root.children == [child]
    assert root.children[0].value == "Child"

def test_add_multiple_children():
    root = TreeNode("Root")
    child1 = TreeNode("Child1")
    child2 = TreeNode("Child2")

    root.add_child(child1)
    root.add_child(child2)

    assert len(root.children) == 2
    assert root.children[0].value == "Child1"
    assert root.children[1].value == "Child2"

def test_remove_child_node():
    root = TreeNode("Root")
    child = TreeNode("Child")
    root.add_child(child)
    root.remove_child(child)

    assert root.children == []


# ---------------------------
# 출력 테스트
# ---------------------------

def test_tree_structure_output():
    root = TreeNode("Root")
    child1 = TreeNode("Child1")
    child2 = TreeNode("Child2")
    child1_1 = TreeNode("Child1-1")

    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(child1_1)

    expected_output = (
        "Root\n"
        "  Child1\n"
        "    Child1-1\n"
        "  Child2\n"
    )

    assert str(root) == expected_output
