# 📚 대규모 시스템에서의 SQL vs NoSQL

## 📖 SQL vs NoSQL – 기본 개념 비교

### 데이터 모델 및 스키마
- **SQL**
  - 테이블 구조의 정형화된 스키마를 사용하며, 데이터를 저장하기 전에 데이터 구조를 미리 정의해야 한다.
  - 각 행은 **레코드**, 각 열은 **속성**으로 구성되며, 구조가 고정되어 있어 스키마가 엄격하다.

- **NoSQL**
  - 문서, 키-값, 컬럼 패밀리, 그래프 등 다양한 데이터 모델을 지원한다.
  - 미리 정의된 스키마 없이 유연한 구조로 데이터를 저장할 수 있어, 애플리케이션의 요구사항에 따라 필드나 구조를 쉽게 변경할 수 있다.
  - 사전에 데이터 구조를 엄격히 설계하지 않아도 되며, 다양한 형태의 비정형 데이터를 저장할 수 있다.


### 관계와 일관성
- **SQL**
  - 테이블 간의 관계를 명확히 정의하며, SQL 쿼리(조인 등)를 통해 복잡한 질의를 처리한다.
  - ACID(원자성, 일관성, 고립성, 지속성) 특성을 준수해 강력한 데이터 일관성을 보장하지만, 트랜잭션 처리 비용이 발생한다.

- **NoSQL**
  - 일반적으로 데이터를 연결하는 관계를 미리 정의하지 않고, 필요에 따라 애플리케이션 계층에서 데이터를 조합한다.
  - ACID보다는 CAP 이론 또는 BASE 철학을 따르는 경우가 많으며, 데이터 일관성보다는 **가용성**과 **분산 환경** 지원에 중점을 둔다.
  - 주로 **결과적 일관성** 모델을 사용하며, 일시적으로 일관성의 지연을 허용하는 대신 분산 환경에서의 높은 성능과 가용성을 제공한다.

### 확장성

- **SQL**
  - 주로 **수직 확장** 방식을 사용
  - 단일 서버의 CPU, 메모리, 디스크 성능을 향상하여 규모 확장
  - 확장 한계가 명확하며 수평 확장에 제한이 있음

- **NoSQL**
  - 주로 **수평 확장** 방식을 사용
  - 여러 대의 서버(노드)를 추가하여 쉽게 용량과 성능 확장 가능
  - 데이터 분산 기술인 **샤딩** 및 복제 기능을 내장하고 있어, 데이터 세트를 여러 노드에 자동으로 분산 및 병렬 처리 가능
  - MongoDB, Cassandra 등이 대표적 사례로, 거의 선형적인 확장 가능
  - 대규모 데이터 및 트래픽 처리에 유리

---

### SQL vs. NoSQL 주요 특징 비교

| 비교 항목      | SQL                                    | NoSQL                                   |
|---------------|---------------------------------------------------|---------------------------------------------------|
| 데이터 모델    | 관계형 (테이블, 행/열)                  | 비관계형 (문서, 키-값, 그래프 등)         |
| 질의 언어      | SQL                       | 고유 API 또는 질의 메커니즘|
| 일관성 모델    | ACID 트랜잭션으로 강력한 일관성 보장                     | CAP 이론 또는 BASE 철학 기반 설계 |
| 확장성 방식    | 주로 수직 확장 (고성능 서버로 규모 확장)<br>수평 확장 제한적 | 수평 확장 용이 (노드 추가로 성능 확장) |
| 성능 특징      | 복잡한 JOIN 및 트랜잭션 지원<br>높은 일관성 유지, 복잡도 증가 시 성능 저하 가능 | 단순 조회/쓰기 고속 처리<br>낮은 지연시간, 실시간 처리 유리 |
| 예시 시스템    | MySQL, PostgreSQL, Oracle, SQLite 등              | MongoDB, Cassandra, Redis, DynamoDB 등            |

---

### 요약

- **SQL 데이터베이스**  
  엄격한 스키마 및 ACID 트랜잭션으로 데이터 무결성과 복잡한 관계 질의가 필요한 경우에 적합

- **NoSQL 데이터베이스**  
  유연한 스키마 및 뛰어난 수평 확장성으로 대규모 데이터와 높은 실시간 처리가 필요한 경우에 유용

## 📖 성능 및 확장성 측면 비교

### 읽기/쓰기 성능

- **SQL**
  - 복잡한 질의(JOIN, 인덱스 활용 등)와 강력한 트랜잭션 지원에서 강점
  - 트랜잭션 무결성 보장을 위한 락 및 WAL(Write-Ahead Log)로 인해 고량의 동시 쓰기 작업에서는 성능이 제한될 수 있음
  - 중간 규모 데이터에서는 적절한 인덱싱 및 쿼리 최적화를 통해 우수한 성능 제공
  - 읽기 부하를 복제본으로 분산하거나 파티셔닝 기법을 통해 성능 최적화 가능

- **NoSQL**
  - 대용량의 단순 읽기/쓰기 작업에 최적화되어 높은 처리량 제공
  - 키 기반의 단순한 데이터 조회 및 쓰기 작업에서 매우 빠른 성능
  - 분산 저장 방식(샤딩)과 병렬 처리를 통해 고속 데이터 삽입 가능
  - 객체 단위로 데이터를 저장하여 JOIN 없이 한 번의 읽기만으로 관련 데이터를 조회해 지연시간 최소화
  - 예시: Cassandra는 초당 수만 건 이상의 연산 처리 가능 (1TB 규모)

### 수평 확장성과 샤딩

- **SQL**
  - 수평 확장이 까다로우며, 데이터 분산 시 JOIN 연산과 트랜잭션 일관성 유지가 복잡
  - 보통 고성능 단일 서버(수직 확장)를 중심으로 운영하며, 읽기 부하만 복제본(Read Replica)을 통해 분산하는 방식을 사용
  - 샤딩(데이터 분할)은 가능하지만 수작업 구성 및 복잡한 애플리케이션 설계 필요
  - 최근 NewSQL과 같은 분산 SQL 시스템도 등장했으나 구현 및 운영 복잡성은 여전히 존재

- **NoSQL**
  - 수평 확장 및 샤딩 기능이 내장되어 있어 손쉽게 노드를 추가하여 성능과 저장 용량을 선형적으로 확장 가능
  - 데이터 분산 및 자동 병렬 처리로 확장 시 성능 저하 최소화
  - 노드 장애 시 다른 노드가 즉시 역할을 대신하는 장애 내성도 높음

### 지연 시간

- **SQL**
  - 단일 서버에서 운영 시 일관된 데이터로 낮은 지연 보장 가능
  - 단, 부하 증가 시 단일 서버 병목 현상으로 응답 시간이 늘어날 가능성 존재
  - 금융 거래처럼 즉각적이고 강한 일관성을 요구하는 작업에서 유리

- **NoSQL**
  - 분산 구조를 통해 글로벌 환경에서 사용자와 가까운 노드로부터 빠른 데이터 제공 가능
  - CDN 등 지역 기반 분산 캐시를 통해 글로벌 서비스에서 지연 시간 최소화 가능
  - 일부 데이터의 최신성(일관성)을 약간 희생하는 대신, 쓰기 지연을 줄이고 높은 처리량 달성 가능 (결과적 일관성)
  - 전 세계적으로 규모가 큰 서비스의 지연 시간을 줄이는 데 효과적

### 요약

- **NoSQL**는 수평 확장, 샤딩, 분산 캐싱을 활용해 높은 처리량과 낮은 지연을 보장하며, 글로벌 규모 서비스에 적합
- **SQL**는 강한 일관성과 복잡한 질의에서 강점을 보이며, 중간 규모의 복잡한 관계 데이터 처리 및 금융 등 강력한 트랜잭션이 필요한 시스템에 적합

## 📖 대규모 사용자 시스템과 실시간 처리에 적합한 DB 비교

### NoSQL 데이터베이스
- **대규모 사용자 및 빅데이터 환경에서 유리**
  - 손쉬운 수평 확장으로 노드 추가 시 성능 유지
  - 소셜 미디어, IoT, 로그 수집, 실시간 분석 시스템 등 급성장하는 서비스에 적합
  - 낮은 지연 시간 및 높은 쓰기 처리량으로 실시간 데이터 처리(실시간 대시보드, 스트리밍 분석)에 강점
  - MongoDB, Cassandra 등은 실시간 빅데이터 분석 및 변화하는 스키마 대응에 탁월
  - 글로벌 서비스(멀티 플레이어 게임, 실시간 광고 추적) 등에서 분산 복제 및 지역별 성능 최적화 가능

### SQL 데이터베이스
- **데이터 무결성과 관계성이 중요한 핵심 비즈니스 데이터 처리에 유리**
  - ACID 트랜잭션 보장 및 복잡한 질의(JOIN 등) 처리에 강점
  - 회원정보, 결제 내역 등 일관성 및 정확성이 핵심적인 데이터 처리에 적합
  - 성숙한 기술 생태계 및 관리 도구의 풍부한 지원으로 안정적인 시스템 운영 가능
  - Google, Facebook, Amazon 등 글로벌 기업들도 핵심 데이터에 SQL을 지속적으로 활용

### 폴리글롯 퍼시스턴스의 활용
- 실무에서는 SQL과 NoSQL을 적절히 혼합하여 사용
  - **SQL 활용 예시**: 회원정보, 권한 관리, 금융 거래, 결제 등 강한 일관성이 필수적인 영역
  - **NoSQL 활용 예시**: 피드 스트림, 캐싱, 로그 데이터, 세션 관리 등 높은 처리량과 실시간 처리 요구 영역
- 시스템 요구사항에 따라 검색엔진(ElasticSearch), 메시지 큐, 캐시(Redis), NewSQL 등 추가 기술과 결합하여 최적의 아키텍처 구성 가능

---

### 주요 활용 사례 요약

| 데이터베이스 유형 | 활용 분야 및 예시 |
|-----------------|----------------|
| **SQL**          | 금융 거래 시스템, 주문/결제 시스템, ERP 등 트랜잭션 무결성과 정형 데이터 처리 |
| **NoSQL**        | 소셜 미디어, 메시징, IoT/센서 데이터 처리, 게임 서버, 콘텐츠 전송(CDN), 실시간 분석 대시보드 등 실시간·대량 데이터 처리 |

---

### 결론
- **“대규모”** 및 “실시간 처리”가 중요한 경우 기본적으로 **NoSQL** 데이터베이스가 적합
- 데이터 구조의 복잡성과 강력한 트랜잭션 무결성이 필요한 경우에는 **SQL** 데이터베이스가 필수적
- 두 가지 DB의 장단점을 이해하고 적절히 혼합하는 전략(**폴리글롯 퍼시스턴스**)이 현실적으로 가장 효율적인 접근법

## 📖 FastAPI에서의 데이터베이스 연동 방법

FastAPI는 비동기 웹 프레임워크로, 다양한 DB 클라이언트 및 ORM과의 연동을 지원합니다.

### SQL 데이터베이스 (PostgreSQL 등)

**주요 사용 ORM 및 클라이언트**

- **SQLAlchemy** (동기 및 비동기 지원, 가장 널리 사용됨)
- **Tortoise ORM** (비동기 전용 ORM)

**SQLAlchemy 사용 예시 (동기)**

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import FastAPI, Depends

DATABASE_URL = "postgresql://username:password@localhost:5432/mydb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/{user_id}")
def read_user(user_id: int, db=Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return user
```

- 요청마다 세션을 관리하며, `Depends`를 활용해 자원 누수 방지
- 비동기 사용 시 `create_async_engine` 및 `AsyncSession` 사용 가능

### NoSQL 데이터베이스 (MongoDB 등)

**주요 사용 클라이언트**

- **Motor** (MongoDB 비동기 공식 클라이언트)

**Motor 사용 예시**

```python
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
client = AsyncIOMotorClient("mongodb://localhost:27017")
users_col = client["mydatabase"]["users"]

class UserModel(BaseModel):
    name: str
    email: str

@app.post("/users")
async def create_user(user: UserModel):
    result = await users_col.insert_one(user.dict())
    return {"id": str(result.inserted_id)}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user = await users_col.find_one({"_id": user_id})
    return user
```

- 비동기 방식으로 성능 극대화 가능
- Pydantic과의 결합으로 직관적인 API 설계 용이

## 📖 FastAPI 백엔드 성능 최적화 실용 조언

- **비동기 I/O 적극 활용**
  - asyncpg(PostgreSQL), Motor(MongoDB) 등 비동기 드라이버 사용

- **커넥션 풀(Connection Pool) 관리**
  - DB 연결을 풀로 관리하여 오버헤드 최소화

- **쿼리 최적화 및 인덱스 활용**
  - 꼭 필요한 데이터만 조회하고, 자주 조회하는 컬럼에 인덱스 추가

- **캐싱 계층 도입**
  - Redis 등을 활용해 자주 쓰이는 데이터 캐싱으로 성능 향상

- **의존성 주입으로 리소스 관리**
  - FastAPI의 `Depends`를 활용하여 세션 관리 자동화 및 자원 누수 방지

- **CPU 집약적 작업 분리**
  - 백그라운드 작업(FastAPI BackgroundTasks, Celery)을 활용해 서버 응답성 유지

- **트래픽 분리 및 모니터링**
  - 읽기/쓰기 트래픽 분리(마스터-슬레이브 복제 등) 및 모니터링 도구(APM)를 사용하여 성능 병목 개선

---
