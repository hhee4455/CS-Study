# 📚 Creational Patterns(생성 패턴)이란?
생성 패턴은 객체 생성 메커니즘에 중점을 둔 패턴 그룹으로,  
반복되는 객체 생성 문제를 상황에 맞게 다루는 솔류션을 제공한다.  

이러한 패턴들은 코드의 모듈성, 유지보수성, 확장성을 향상시키며,  
객체 생성 방식을 효율적으로 관리하여 성능과 코드 구조를 개선하는 데 도움이 된다.

### 대표적인 다섯 가지 생성 패턴
- 싱글톤
- 팩토리 매서드
- 추상 팩토리
- 빌더
- 프로토타입 패턴

---

## 싱글톤 패턴
싱글톤 패턴은 특정 클래스의 인스턴스를 오직 하나만 생성되도록 보장하고,  
그 인스턴스에 전역적으로 접근할 수 있는 글로벌 접근점을 제공하는 패턴이다.  

시스템 전체에서 하나뿐인 객체를 만들어 여러 곳에서 공유해야 할 때 사용하는 설계 패턴이다.  

이 패턴을 적용하면 동일 클래스에 대해 반복된 객체 생성을 피하고,  
하나의 인스턴스를 재사용함으로써 리소스를 절약할 수 있다.

### 주요 특징
- 유일한 인스턴스 보장: 클래스 당 단 하나의 객체만 생성됨을 보증한다.
- 전역 접근점 제공: 어디서든 이 인스턴스에 접근할 수 있어 공유 자원처럼 활용할 수 있다.
- 생성 과정의 제어: 클래스 내부에서 인스턴스 생성 여부를 제어하므로, 필요 시 지연 초기화나 스레드 안전 처리 등을 구현할 수 있다.

### 사용시기
- 공통 자원 관리 : 설정 정보, 로그 관리 등 애플리케이션 전역에서 하나만 있어야 하는 객체가 있을 때
- 비용이 큰 리소스 : 생성 비용이 큰 리소스를 매번 생성하지 않고 하나만 만들어 공유하고 싶을 때
- 상태 공유가 필요할 때 : 캐시, 설정, 상태 등 여러 컴포넌트가 동일한 상태나 데이터를 공유해야 할 때

싱글톤을 사용할 때는 전역 상태 공유로 인한 의존성 결합이나 멀티스레드 환경에서 동시성 문제가 발생하지 않도록 주의가 필요하다.

### 문제점
싱글턴 패턴은 한 번에 두 가지의 문제를 동시에 해결함으로써 단일 책임 원칙을 위반한다.

- 클래스에 인스턴스가 하나만 있도록 한다.
- 해당 인스턴스에 대한 전역 접근 지점을 제공 한다.

최근에는 싱글턴 패턴이 워낙 대중화되어 패턴이 나열된 문제 중 한 가지만 해결하더라도 그것을 싱글턴이라고 부를 수 있다.

### 사용 예시 (FastAPI)
FastAPI 애플리케이션에서는 싱글톤 패턴이 데이터베이스 연결 공유나 외부 서비스 클라이언트 재사용 등에 활용될 수 있다.  

예를 들어, 데이터베이스 연결은 설정과 초기화 비용이 큰 리소스인데,   
각 요청마다 새로운 연결을 생성하는 것은 비효율적이다.  

대신 싱글톤 패턴으로 공용 DB 연결 풀을 구성해 애플리케이션 시작 시 하나만 생성하고 요청마다 이를 사용하도록 하면 효율을 높일 수 있다.

FastAPI와 PyMongo를 사용하여 MongoDB 데이터베이스 클라이언트를 싱글톤으로 관리하는 예시
```python
from fastapi import FastAPI, Depends
from pymongo import MongoClient

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # MongoDB 클라이언트 초기화 (애플리케이션 전체에서 하나만 생성)
            cls._instance.client = MongoClient("mongodb://localhost:27017/")
            cls._instance.db = cls._instance.client["mydatabase"]
        return cls._instance

# 의존성 주입용 함수
def get_db() -> Database:
    return Database()

app = FastAPI()

@app.get("/data")
def get_data(db: Database = Depends(get_db)):
    # 싱글톤 DB 인스턴스를 통해 데이터 조회
    result = db.db.my_collection.find_one({})
    return {"result": result}
```

위 코드에서 `Database` 클래스는 싱글톤으로 구현되어,  
`Database()` 호출 시 항상 동일한 인스턴스를 반환한다.  

FastAPI의 `Depends`를 이용한 `get_db` 함수를 통해 라우트 함수에 `Database` 인스턴스를 주입하면,  
각 요청마다 동일한 DB 연결(MongoClient)을 재사용하게 됩니다​.

이를 통해 불필요한 연결 생성 비용을 줄이고,  
하나의 애플리케이션 프로세스 내에서는 DB 연결이 공유되어 자원 효율성과 성능을 향상시킬 수 있다.

---

## 팩토리 메서드 패턴
팩토리 메서드 패턴은 객체 생성 처리를 서브클래스로 분리하여,  
객체 생성의 인터페이스만 정의하고 실제 생성될 객체의 타입 결정은 하위 클래스에 맡기는 방식을 말한다.  

즉, 클래스 간 상속 관계에서 부모 클래스는 제품 객체를 생성하는 인터페이스만 제공하고,  
구체적인 생성 과정은 자식 클래스가 구현한다.  

이렇게 함으로써 객체 생성 코드를 클라이언트로부터 숨기고,  
객체 생성과 사용의 분리 및 확장성을 얻을 수 있다.

### 주요 특징
- 객체 생성의 캡슐화: 객체를 생성하는 코드를 별도의 메서드로 추상화하여, 상속을 통해 다양한 객체 생성 방식을 정의할 수 있다.
- 확장 용이성: 새로운 종류의 객체를 생성해야 할 경우, 기존 코드를 수정하지 않고 새로운 서브클래스를 추가하여 팩토리 메서드를 구현하면 된다.
- 런타임 다형성: 실행 시점에 생성될 객체의 구체적인 클래스가 결정되므로, 조건에 따라 다양한 객체를 유연하게 생성할 수 있다.

### 사용시기
- 구체 클래스의 결정이 런타임에 이루어질 때
- 객체 생성 로직을 공통화하고 싶을 때
- 코드 확장성을 높이고 싶을 때

### 구현 예시(FastAPI)
FastAPI와 같은 웹 프레임워크에서 팩토리 메서드 패턴은 동적 객체 생성이 필요한 상황에서 응용될 수 있다.  
예를 들어, 결제 API를 구현한다고 가정하면, 결제 방식에 따라 서로 다른 결제 처리 객체를 생성해야 한다고 가정하면,  
팩토리 메서드 패턴을 이용해 이를 유연하게 처리할 수 있다. 

사용자가 요청한 결제 수단에 따라 다른 결제 프로세서 객체를 생성하는 예시

```python
from fastapi import FastAPI, HTTPException

class PaymentProcessor:
    def process_payment(self, amount: float) -> str:
        raise NotImplementedError()

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"신용카드로 {amount}달러 결제 처리"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"PayPal로 {amount}달러 결제 처리"

class PaymentProcessorFactory:
    @staticmethod
    def create_processor(method: str) -> PaymentProcessor:
        if method == "credit_card":
            return CreditCardProcessor()
        elif method == "paypal":
            return PayPalProcessor()
        else:
            # 지원하지 않는 결제 방식에 대한 예외 처리
            raise HTTPException(status_code=400, detail="유효하지 않은 결제 방식입니다.")

app = FastAPI()

@app.post("/pay/{method}")
def pay(method: str, amount: float):
    processor = PaymentProcessorFactory.create_processor(method)
    result = processor.process_payment(amount)
    return {"result": result}
```

`PaymentProcessorFactory.create_processor`가 팩토리 메서드의 역할을 한다.  
전달된 `method` 문자열에 따라 `CreditCardProcessor`나 `PayPalProcessor`와 같은 적절한 하위 클래스 인스턴스를 생성하여 반환한다.  

FastAPI 경로 함수인 `pay`에서는 URL 경로 매개변수로 결제 방식을 받아서 팩토리 메서드를 호출하고,  
반환된 객체의 `process_payment`를 실행함으로써 결제 처리를 수행 한다.

이를 통해 클라이언트의 입력이나 조건에 따라 객체 생성을 유연하게 처리할 수 있으며,  
새로운 결제 방식이 추가되더라도 `PaymentProcessor`의 하위 클래스와 팩토리의 분기만 추가하면 손쉽게 확장할 수 있다. 

이처럼 팩토리 메서드 패턴은 FastAPI 컨트롤러에서 결정 로직과 객체 생성 로직을 분리하는 데 활용되어, 코드의 가독성과 관리 효율을 높여준다.

---

## 추상 팩토리
추상 팩토리 패턴은 관련성이 있는 여러 종류의 객체군을 생성하기 위한 인터페이스를 제공하며,  
구체적인 클래스는 지정하지 않고도 일련의 객체들을 생성할 수 있도록 해주는 패턴입니다​. 

여러 개의 서로 연관된 객체들을 함께 만들어야 할 때,  
추상 팩토리를 이용하면 호환되는 제품 객체들을 일관된 방식으로 생성할 수 있고,  
제품군 교체 시에도 한 번에 변경이 가능합니다.

### 주요 특징
- 제품군 생산: 한 번의 호출로 관련된 여러 객체를 생성하여 추상적인 제품군을 이룰 수 있다.
- 구현으로부터의 독립: 객체들의 구체적인 클래스 이름을 코드에서 직접 사용하지 않고도 생성할 수 있어, 클라이언트 코드가 제품들의 구상 클래스에 독립적이다.
- 대체 가능성: 특정 제품군을 생성하는 공장을 교체함으로써 전체 제품군을 쉽게 교체할 수 있다.

### 사용 시기
- 서로 관련된 여러 객체를 함께 생성해야 할 때
- 환경에 따라 구현체를 바꿔야 할 때
- 제품군 교체를 용이하게 하고 싶을 때

### 구현 예시(FastAPI)
FastAPI 애플리케이션에서 추상 팩토리 패턴은 구성 가능하고 교체 가능한 컴포넌트 집합을 만들어야 할 때 활용할 수 있다.  

예를 들어, 애플리케이션이 다양한 환경에서 동작해야 해서 데이터 저장소를 파일 시스템과 클라우드 스토리지 둘 다 지원해야 한다고 가정해보자.  

이를 위해 추상 팩토리를 정의하고, 각 환경에 맞는 구체 팩토리를 구현할 수 있다.

- 추상 팩토리 예시: `StorageFactory`라는 추상 클래스를 만들어 `create_file_dao()`, `create_user_dao()` 등의 메서드를 정의한다.
- 로컬 파일 시스템 구현: `LocalStorageFactory`는 `StorageFactory`를 상속하여 파일 시스템을 사용하는 DAO들을 생성한다.
- 클라우드(예: AWS S3) 구현: `S3StorageFactory`는 S3 SDK를 활용하여 동일한 DAO 인터페이스를 구현하는 객체들을 생성한다.

애플리케이션은 설정에 따라 `StorageFactory`의 구현체 중 하나를 선택해 사용하고,  
FastAPI의 엔드포인트 로직에서는 추상화된 DAO를 통해 데이터 조작을 수행한다.  

이렇게 하면 코드베이스는 추상 인터페이스에만 의존하므로,  
환경(로컬 ↔ 클라우드) 전환이 필요할 때 팩토리 교체만으로 전체 관련 객체군이 교체되어 동작하게 된다. 

---

## 빌더 패턴
빌더 패턴은 복잡한 객체의 생성 과정을 객체의 표현(표현 방식)과 분리하여,  
동일한 생성 절차에서 서로 다른 표현의 객체를 만들 수 있도록 돕는 패턴티다.  

즉, 객체를 구성하는 과정(단계)을 빌더라는 별도 객체로 캡슐화함으로써,  
구성 단계의 순서나 방식은 일정하게 유지하면서도 결과물은 다양한 형태를 가질 수 있게 해준다.

### 주요 특징
- 복잡한 객체 생성 단계 분리: 객체 생성에 여러 단계가 필요하고 설정 옵션이 많은 경우, 빌더를 통해 단계를 하나씩 쌓아 올리듯 구성할 수 있다.
- 다양한 표현의 객체 생성: 동일한 빌더 절차를 거쳐서도 빌더의 구성에 따라 서로 다른 구성의 객체를 생성할 수 있다.
- 메서드 체이닝 지원: 빌더를 구현할 때 메서드 체이닝을 활용하면, 객체 생성 과정을 유창하게 기술할 수 있다. 

### 사용 시기
- 매우 복잡한 객체를 생성해야 할 때
- 객체의 다양한 버전을 생성해야 할 때
- 객체 생성 과정에서 중간 상태 검증이나 단계적 처리가 필요할 때

### 구현 예시(FastAPI)
웹 애플리케이션 개발에서도 빌더 패턴이 응용될 수 있는 시나리오가 있다.  

예를 들어 쿼리 빌더를 생각해볼 수 있다.  
FastAPI 엔드포인트에서 사용자의 여러 필터 조건에 따라 데이터베이스 쿼리를 동적으로 생성해야 한다면,  
빌더 객체를 사용하여 조건을 추가하는 메서드를 단계적으로 호출해 최종 쿼리를 생성할 수 있다.

예를 들어, 검색 API에서 사용자로부터 name, age, location 등의 여러 필터를 입력받는다면

```python
class UserQueryBuilder:
    def __init__(self):
        self.query = {}
    def filter_name(self, name: str):
        if name:
            self.query["name"] = name
        return self
    def filter_age(self, min_age: int = None, max_age: int = None):
        if min_age is not None:
            self.query["age"] = {"$gte": min_age}
        if max_age is not None:
            self.query.setdefault("age", {})["$lte"] = max_age
        return self
    def filter_location(self, location: str):
        if location:
            self.query["location"] = location
        return self
    def build(self) -> dict:
        return self.query

# FastAPI 엔드포인트에서의 사용 예시
@app.get("/users/search")
def search_users(name: str = None, min_age: int = None, max_age: int = None, location: str = None):
    query = (UserQueryBuilder()
                .filter_name(name)
                .filter_age(min_age, max_age)
                .filter_location(location)
                .build())
    results = users_collection.find(query)  # MongoDB 예시: 동적으로 생성된 쿼리 사용
    return {"query": query, "results": list(results)}
```

이러한 `UserQueryBuilder`는 여러 조건을 조합하여 MongoDB 쿼리 문서를 생성하는 빌더의 한 예이다.  

각 조건 필터 메서드는 설정 값이 주어졌을 때만 쿼리에 해당 조건을 추가하고,  
빌더 객체 자신을 반환하여 다음 조건을 체이닝할 수 있게 한다. 

최종적으로 `build()`를 호출하면 누적된 조건으로 이루어진 쿼리 딕셔너리를 반환한다.

이를 통해 엔드포인트 함수에서는 복잡한 if-분기 대신 빌더를 활용하여 가독성 좋게 쿼리를 조립할 수 있다.  

마찬가지로, 응답을 구성할 때 여러 조각의 데이터를 결합하거나 외부 서비스 호출 결과들을 모아 하나의 응답 객체를 만들어야 할 때도 빌더를 응용할 수 있다.
 
예를 들어 여러 API를 호출하여 취합한 응답을 단계적으로 빌드하거나,  
PDF/리포트 생성 시 빌더 패턴으로 섹션을 추가해가는 식의 응용도 생각해볼 수 있다.

요컨대 빌더 패턴은 FastAPI 컨텍스트에서 복잡한 결과 생성이나 다단계 객체 구성이 필요한 경우 코드 구조를 깔끔하게 하고,  
각 단계별 처리를 관리하기 쉽게 해주는 도구가 될 수 있다.

---

## 프로토타입 패턴
프로토타입 패턴은 이미 존재하는 객체를 복제(clone)하여 새로운 객체를 생성하는 방식의 패턴이다.  

즉, 클래스의 인스턴스를 새로 생성하는 대신, 미리 준비된 견본 객체를 복사하여 초기 상태가 갖춰진 객체를 얻는 방법이다.  

이 패턴은 객체 생성 비용이 큰 경우에 유용하며, 복제된 객체를 독립적으로 수정하여 사용할 수 있다.

### 주요 특징
- 객체 복제를 통한 생성: 기존 객체를 복사해서 새로운 객체를 만들므로, 복잡한 초기 설정이나 연산을 매번 수행하지 않아도 된다.
- 런타임 동적 객체 생성: 런타임에 객체의 구체적인 클래스를 모르는 경우에도, 해당 객체를 프로토타입으로 복제함으로써 동일한 타입의 객체를 쉽게 생성할 수 있다.
- 얕은 복사 vs 깊은 복사: 복제 시 얕은 복사인지 깊은 복사인지에 따라 복제된 객체의 내부 참조 처리 방식이 달라진다.

### 사용 시기
- 객체 생성 비용이 매우 큰 경우
- 동일한 객체를 다수 생성해야 하는 경우
- 클래스로부터 생성할 수 없는 객체가 있을 때

### 구현 예시(FastAPI)
FastAPI와 같은 웹 애플리케이션에서 프로토타입 패턴은 상대적으로 덜 직접적으로 쓰이지만,  
적절한 상황에서 활용하면 성능 최적화나 코드 단순화를 얻을 수 있다.

- 초기 설정이 복잡한 객체의 재사용
- 기본 응답 템플릿 복제

아래와 같이 미리 기본 응답 객체를 만들어 두고 매 요청마다 복제하여 사용하는 방식을 생각해볼 수 있다.

```python
from pydantic import BaseModel

# 응답용 Pydantic 모델 정의
class BaseResponse(BaseModel):
    status: str = "ok"
    data: dict = {}

# 애플리케이션 기동 시 프로토타입 인스턴스 생성
base_response_proto = BaseResponse()

@app.get("/info/{item_id}")
def get_info(item_id: str):
    # 프로토타입 응답 객체 복제
    resp = base_response_proto.copy(deep=True)
    # 요청별 데이터 채워넣기
    resp.data = {"item_id": item_id, "detail": fetch_detail(item_id)}
    return resp
```

위 코드에서 `base_response_proto`는 응답용 객체의 프로토타입이며,  
각 요청 시 `.copy(deep=True)`를 호출해 새로운 인스턴스를 얻은 후 필요한 데이터를 채워 응답한다.  

이렇게 하면 `BaseResponse` 모델의 초기화 비용을 한 번만 치르고,  
이후에는 복제를 통해 사용하게 되므로 약간의 성능 향상을 기대할 수 있다.  

물론 이 패턴을 남용할 경우 코드 복잡도가 높아질 수 있으므로,  
진짜 객체 생성 비용이 병목이 되는 경우에 한해 제한적으로 사용하는 것이 좋다.  

FastAPI에서는 대개 싱글톤 패턴이나 캐싱이 더 자주 활용되지만,  
프로토타입 패턴도 특정 상황에서 객체 생성 비용 최적화를 위해 고려해볼 수 있는 도구이다.