# 📚 GROUP BY와 CTAS

## 📖 GROUP BY와 AGGREGATE 함수

### GROUP BY와 AGGREGATE 함수
- 테이블 레코드를 그룹핑하여 그룹별로 다양한 정보를 계산
- 먼저 그룹핑을 할 필드를 결정 (하나 이상)
    - GROUP BY로 지정(필드이름,일련번호)
- 다음 그룹별로 계산할 내용을 결정
    - 여기서 Aggregate 함수를 사용
    - COUNT, SUM, AVG, MIN, MAX, LISTAGG, ...

- 월별 세션수를 계산하는 SQL
``` sql
SELECT 
    LEFT(ts,7) AS mon,
    COUNT(1) AS session_count
FROM raw_data.session_timestamp
GROUP BY 1
ORDER BY 1;
```

### 문제 1 : 가장 많이 사용된 채널은 무엇인가?
- 가장 많이 사용되었다는 정의 : 사용자 기반 아니면 세션 기반?

``` sql
SELECT
    channel,
    COUNT(1) AS session_count,
    COUNT(DISTINCT userID) AS user_count
FROM raw_data.user_session_channel
GROUP BY 1
ORDER BY 2 DESC;
```

### 문제 2 : 가장 많은 세션을 만들어낸 사용자 ID는 무엇인가?
- 필요한 정보 - 세션 정보, 사용자 정보

``` sql
SELECT
    userID,
    COUNT(1) AS count
FROM raw_data.user_session_channel
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
```

### 문제 3 : 월별 유니크한 사용자 수
- 이게 바로 MAU에 해당
- 필요한 정보 - 시간 정보, 사용자 정보

``` sql
SELECT
    TO_CHAR(A.ts,'YYYY-MM') AS month,
    COUNT(DISTINCT B.userid) AS mau -- COUNT의 동작을 잘 이해하는 것이 중요, DISTINCT와 연동
FROM raw_data.session_timestamp A
JOIN raw_data.user_session_channel B -- INNER JOIN vs LEFT JOIN
ON A.sessionid = B.sessionid
GROUP BY 1
ORDER BY 1 DESC;
```

### 문제 4 : 월별 채널별 유니트한 사용자 수
- 필요한 정보 - 시간 정보, 사용자 정보, 채널 정보

``` sql
SELECT
    TO_CHAR(A.ts, 'YYYY-MM') AS month,
    channel,
    COUNT(DISTINCT B.userid) AS mau
FROM raw_data.session_timestamp A
JOIN raw_data.user_session_channel B
ON A.sessionid = B.sessionid
GROUP BY 1,2
ORDER BY DESC,2;
```

## 📖 CTAS와 CTE 소개

### CTAS: SELECT를 가지고 테이블 생성
- 간단하게 새로운 테이블을 만드는 방법
- 자주 조인하는 테이블들이 있다면 이를 CTAS를 사용해서 조인해두면 편리해짐

### 항상 시도해봐야하는 데이터 품질 확인 방법들
- 중복된 레코드들 체크하기
- 최근 데이터의 존재 여부 체크하기
- Primary key uniqueness가 지켜지는지 체크하기
- 값이 비어있는 컬럼들이 있는지 체크하기

### 중복된 레코드 체크하기
- 두개의 카운트를 비교

``` sql
SELECT COUNT(1)
FROM session_summary;

SELECT COUNT(1)
FROM (
    SELECT DISTINCT userId, sessionId, ts, channel
    FROM session_summary
);
```

- CTE를 사용해서 중복 제거 후 카운트 해보기

``` sql
With ds AS (
    SELECT DISTINCT userId, sessionId, ts, channel
    FROM session_summary
)
SELECT COUNT(1)
FROM ds;
```

### 최근 데이터 존재 여부 확인하기

``` sql
SELECT MIN(ts), MAX(ts)
FROM session_summary;
```

### Primary key uniqueness가 지켜지는지 체크하기

``` sql
SELECT sessionId, COUNT(1)
FROM session_summary
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
```

### 값이 비어있는 컬럼들이 있는지 체크하기

``` sql
SELECT
    COUNT(CASE WHEN sessionId is NULL THEN 1 END) sessionid_null_count,
    COUNT(CASE WHEN userId is NULL THEN 1 END) userid_null_count,
    COUNT(CASE WHEN ts is NULL THEN 1 END) ts_null_count,
    COUNT(CASE WHEN channel is NULL THEN 1 END) channel_null_count
FROM session_summary;
```