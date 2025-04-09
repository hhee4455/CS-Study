# 📚 대규모 시스템에서의 SQL vs NoSQL

## 📖 SQL vs NoSQL – 기본 개념 비교

### 데이터 모델 및 스키마
- **SQL**
  - 테이블 구조의 정형화된 스키마 사용
  - 각 행: **레코드**, 각 열: **속성**으로 구성
- **NoSQL**
  - 문서, 키-값, 컬럼 패밀리, 그래프 등 다양한 모델 지원
  - 유연한 구조로 비정형 데이터 저장 가능

### 관계와 일관성
- **SQL**
  - 테이블 간 명확한 관계, 복잡한 질의 지원
  - **ACID** 특성으로 강력한 일관성 보장
- **NoSQL**
  - 관계 미정의, 애플리케이션 계층에서 조합
  - **CAP 이론** 또는 **BASE 철학**, 결과적 일관성 추구

### 확장성
- **SQL**
  - **수직 확장** 중심, 수평 확장 제한적
- **NoSQL**
  - **수평 확장** 용이, 샤딩 및 복제 기능 내장

## 📖 SQL vs. NoSQL 주요 특징 비교

| 항목         | SQL                                      | NoSQL                                   |
|--------------|-------------------------------------------|-----------------------------------------|
| 데이터 모델   | 관계형 (테이블, 행/열)                   | 비관계형 (문서, 키-값, 그래프 등)       |
| 질의 언어     | SQL 표준                                 | 고유 API 또는 질의 메커니즘            |
| 일관성 모델   | ACID 트랜잭션                            | CAP/BASE, 결과적 일관성                 |
| 확장성 방식   | 수직 확장                                 | 수평 확장                               |
| 성능 특징     | 복잡한 JOIN 및 트랜잭션 지원             | 단순 조회/쓰기 고속 처리               |
| 예시 시스템   | MySQL, PostgreSQL, Oracle                | MongoDB, Cassandra, Redis, DynamoDB    |

## 📖 성능 및 확장성 측면 비교

### 읽기/쓰기 성능
- **SQL**: 트랜잭션 무결성, 인덱싱 최적화, 읽기 부하 분산 가능
- **NoSQL**: 단순 읽기/쓰기 최적, 병렬 삽입 및 고속 처리

### 수평 확장성과 샤딩
- **SQL**: 수평 확장 어려움, 샤딩은 복잡
- **NoSQL**: 샤딩 내장, 노드 추가로 성능 유지

### 지연 시간
- **SQL**: 낮은 지연 가능하나 병목 발생 우려
- **NoSQL**: 지연 최소화, 지역 기반 분산 지원

## 📖 대규모 사용자 시스템과 실시간 처리에 적합한 DB 비교

### NoSQL 데이터베이스
- 수평 확장 용이
- 실시간 대시보드, 스트리밍 분석 등에 강점
- MongoDB, Cassandra 등

### SQL 데이터베이스
- 데이터 무결성과 복잡한 질의에 강점
- 회원정보, 결제 내역 등 핵심 데이터에 적합

### 폴리글롯 퍼시스턴스
- **SQL**: 트랜잭션, 정형 데이터 처리
- **NoSQL**: 피드, 캐싱, 로그 등 대규모 처리
- ElasticSearch, Redis, 메시지 큐 등과 조합 가능

## 📖 주요 활용 사례 요약

| DB 유형     | 활용 분야 및 예시                                               |
|-------------|------------------------------------------------------------------|
| SQL         | 금융, 결제, ERP, 정형 데이터                                    |
| NoSQL       | 소셜, 메시징, IoT, 게임, CDN, 실시간 분석 등 대량 데이터 처리   |

## 📖 결론
- 대규모/실시간 처리 → **NoSQL**
- 정합성/트랜잭션 중심 → **SQL**
- 실무에서는 혼합 전략(폴리글롯 퍼시스턴스) 활용이 이상적

---

## 📖 FastAPI에서의 데이터베이스 연동 방법

### SQL 데이터베이스 (PostgreSQL 등)

- 주요 ORM: `SQLAlchemy`, `Tortoise ORM`

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

### NoSQL 데이터베이스 (MongoDB 등)
- 주요 클라이언트: `Motor`

``` python
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