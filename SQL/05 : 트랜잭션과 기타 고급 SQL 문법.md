# 📚 트랜잭션과 기타 고급 SQL 문법

## 📖 트랜잭션 소개와 실습

### 트랜잭션이란?
- Atomic하게 실행되어야 하는 SQL들을 묶어서 하나의 작업처럼 처리하는 방법
    - 이는 DDL이나 DML 중 레코드를 수정/추가/삭제할 것에만 의미가 있음
    - SELECT에는 트랜잭션을 사용할 이유가 없음
    - BEGIN과 END 혹은 BEGIN과 COMMIT 사이에 해당 SQL들을 사용
    - ROLLBACK

- 은행 계좌 이체가 아주 좋은 예
    - 계좌 이체 : 인출과 입금의 두 과정으로 이뤄짐
    - 만일 인출은 성공했지만 입금이 실패한다면?
    - 이 두과정은 동시에 성공하던지 실패해야함 -> Atomic하다는 의미
    - 이런 과정들을 트랜잭션으로 묶어주어야함
    - 조회만 한다면 이는 트랜잭션으로 묶일 이유가 없음

``` sql
BEGIN;
    A의 계좌로부터 인출;  -- 마치 하나의 명령러처럼 처리됨.
    B의 계좌로 입금;
END;
```

- END와 COMMIT은 동일
- 만일 BEGIN 전의 상태로 돌아가고 싶다면 ROLLBACK 실행
- 이 동작은 commit mode에 따라 달라짐

### 트랜잭션 커밋 모드 : autocommit
- autocommit = True
    - 모든 레코드 수정/삭제/추가 작업이 기본적으로 바로 데이터베이스에 쓰여짐. 이를 커밋 된다고 함
    - 만일 특정 작업을 트랜잭션으로 묶고 싶다면 BEGIN과 END(COMMIT)/ROLLBACK으로 처리
- autocommit = False
    - 모든 레코드 수정/삭제/추가 작업이 COMMIT 호출될 때까지 커밋되지 않음

### 트랜잭션 방식
- Google Colab의 트랜잭션
    - 기본적으로 모든 SQL statement가 바로 커밋된 (autocommit = True)
    - 이를 바꾸고 싶다면 BEGIN;END; 혹은 BEGIN;COMMIT을 사용 (혹을 ROLLBACK;)
- psycopg2 의 트랜잭션
    - autocommit이라는 파라미터로 조절가능
    - autocommit=True가 되면 기본적으로 PostgreSQL의 커밋 모드와 동일
    - autocommit=False가 되면 커넥션 객체의 .commit()과 .rollback() 함수로 트랜잭션 조절 가능

### DELETE FROM vs. TRUNCATE
- DELETE FROM table_name(not DELETE * FROM)
    - 테이블에서 모든 레코드 삭제
    - vs. DROP TABLE table_name
    - WHERE을 사용해 특정 레코드만 삭제 가능

- TRUNCATE table_name도 테이블에서 모든 레코드를 삭제
    - DELETE FROM은 속도가 느림
    - TRUNCATE이 전체 테이블의 내용 삭제시에는 여러모로 유리
    - 하지만 두가지 단점이 존재
        - WHERE을 지원하지 않음
        - Transaction을 지원하지 않음

## 📖 기타 고급 문법 소개와 실습

### 알아두면 유용한 SQL 문법들
- UNION, EXCEPT, INTERSECT
- COALESCE, NULLIF
- LISTAGG
- LAG
- WINDOW 함수
- ROW_NUMBER OVER
- SUM OVER
- FIRST_VALUE, LAST_VALUE
- JSON Parsing 함수

### UNION, EXCEPT, INTERSECT
- UNION(합집합)
    - 여러개의 테이블들이나 SELECT 결과를 하나의 결과로 합쳐줌
    - UNION vs UNION ALL : UNION은 중복을 제거

- EXCEPT(MINUS)
    - 하나의 SELECT 결과에서 다른 SELECT 결과를 빼주는 것이 가능

- INTERSECT(교집합)
    - 여러 개의 SELECT문에서 같은 레코드들만 찾아줌

### COALESCE, NULLIF
- CLALESCE(Expression1, Expression2, ...)
    - 첫번째 Expression 부터 값이 NULL이 아닌 것이 나오면 그 값을 리턴하고 모두 NULL이면 NULL을 리턴한다.
    - NULL 값을 다른 값으로 바꾸고 싶을 때 사용한다.

- NULLIF(Expression1, Expression2)
    - Expression1과 Expression2의 값이 같으면 NULL을 리턴한다.

### LISTAGG
- GROUP BY에서 사용되는 Aggregate 함수 중의 하낟
- 사용자 ID 별로 채널을 순서대로 리스트:

``` sql
SELECT
    userid,
    LISTAGG(channel) WITHIN GROUP (ORDER BY ts) channels
FROM raw_data.user_session_channel usc
JOIN raw_data.session_timestamp st 
ON usc.sessionid = st.sessionid
GROUP BY 1
LIMIT 10;
```

``` sql
SELECT
    userid,
    LISTAGG(channel, '->') WITHIN GROUP (ORDER BY ts) channels
FROM raw_data.user_session_channel usc
JOIN raw_data.session_timestamp st 
ON usc.sessionid = st.sessionid
GROUP BY 1
LIMIT 10;
```

### WINDOW
- Syntax
    -function(expression) OVER ([PARTITION BY expression][ORDER BY expression])

- Useful functions
    - ROW_NUMBER, FIRST_VALUE, LAST_VALUE, LAG
    - Math functions: AVG, SUM, COUNT, MAX, ...

### JSON Parsing Function
- JSON의 포맷을 이미 아는 상황에서만 사용 가능한 함수
    - JSON String을 입력으로 받아 특정 필드의 값을 추출가능(nested 구조 지원)