import pytest
import sys
import os

# 모듈 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DS_07_hash import HashTable


# ---------------------------
# 정상 동작 테스트
# ---------------------------

def test_insert_and_get():
    ht = HashTable(5)
    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("orange", 300)

    assert ht.get("apple") == 100
    assert ht.get("banana") == 200
    assert ht.get("orange") == 300
    assert ht.size == 3

def test_update_value():
    ht = HashTable(5)
    ht.insert("apple", 100)
    ht.insert("apple", 500)  # 값 업데이트

    assert ht.get("apple") == 500
    assert ht.size == 1  # 크기는 증가하지 않아야 함

def test_collision_handling():
    ht = HashTable(2)  # 충돌을 강제로 유발하기 위해 테이블 크기를 작게 설정
    ht.insert("key1", 1)
    ht.insert("key2", 2)  # 다른 키지만 같은 인덱스 가능성 높음

    # 둘 다 정상적으로 조회되어야 함
    assert ht.get("key1") == 1
    assert ht.get("key2") == 2


# ---------------------------
# 삭제 동작 테스트
# ---------------------------

def test_delete_existing_key():
    ht = HashTable(5)
    ht.insert("apple", 100)
    ht.insert("banana", 200)

    ht.delete("apple")
    assert ht.size == 1
    with pytest.raises(KeyError, match="키를 찾을 수 없습니다"):
        ht.get("apple")

def test_delete_non_existing_key():
    ht = HashTable(5)
    ht.insert("apple", 100)

    with pytest.raises(KeyError, match="삭제할 키를 찾을 수 없습니다"):
        ht.delete("banana")


# ---------------------------
# 출력 테스트
# ---------------------------

def test_str_output():
    ht = HashTable(5)
    ht.insert("apple", 100)
    output = str(ht)

    # 출력 문자열에 키-값 쌍이 포함되어 있어야 함
    assert "apple" in output
    assert "100" in output
