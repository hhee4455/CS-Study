# 📚 OSI 모델이란?
- **네트워크 통신 기능을 7개 계층으로 나눈 개념적 프레임워크**
- **서로 다른 컴퓨터 시스템이 원활하게 통신할 수 있도록 표준을 제공**

<img src="../image/Networking/1_1.png" alt="설명" width="400" style="display: block; margin: auto;">
<br>

## 📌 OSI 모델의 7계층

### 7. 애플리케이션 계층
- 사용자 데이터와 직접 상호 작용하는 유일한 계층
- 소프트웨어가 사용자에게 의미 있는 데이터를 제공하기 위해 사용하는 프로토콜과 데이터 처리 담당
- **프로토콜:** HTTP, SMTP(이메일 통신 프로토콜)

<img src="../image/Networking/1_2.png" alt="설명" width="400" style="display: block; margin: auto;">
<br>

### 6. 프레젠테이션 계층
- 애플리케이션 계층이 데이터를 이해할 수 있도록 변환하는 역할
- 데이터의 변환, 암호화, 압축을 담당

<img src="../image/Networking/1_3.png" alt="설명" width="400" style="display: block; margin: auto;">
<br>

### 5. 세션 계층
- 두 기기 간의 통신 세션을 설정, 유지 및 종료하는 역할
- 데이터 전송 중 체크포인트 설정 및 동기화 수행

<img src="../image/Networking/1_4.png" alt="설명" width="400" style="display: block; margin: auto;">
<br>

### 4. 전송 계층
- 두 기기 간 종단 간(end-to-end) 통신을 담당
- 흐름 제어 및 오류 제어 기능 포함
- **프로토콜:** TCP(전송 제어 프로토콜), UDP(사용자 데이터그램 프로토콜)

<img src="../image/Networking/1_5.png" alt="설명" width="400" style="display: block; margin: auto;">
<br>

### 3. 네트워크 계층
- 서로 다른 네트워크 간 데이터 전송을 가능하게 함
- 최적의 경로를 찾아 데이터 패킷을 목적지까지 전달 (라우팅)
- **프로토콜:** IP, ICMP, IGMP, IPsec

<img src="../image/Networking/1_6.png" alt="설명" width="400" style="display: block; margin: auto;">
<br>

### 2. 데이터 링크 계층
- 동일한 네트워크 내 두 장치 간 데이터 전송을 담당
- 인트라 네트워크 통신에서 흐름 제어 및 오류 제어 기능 수행

<img src="../image/Networking/1_7.png" alt="설명" width="400" style="display: block; margin: auto;">
<br>

### 1. 물리적 계층
- 케이블, 스위치 등 데이터 전송과 관련된 물리적 장비 포함
- 데이터를 0과 1의 비트 스트림으로 변환

<img src="../image/Networking/1_8.png" alt="설명" width="400" style="display: block; margin: auto;">
<br>


## 💭 면접 예상 질문
 ❓ 질문 | ✅ 답변 |
|--------|--------|
| **7계층으로 나눈 이유는?** | 계층을 분리하여 네트워크 설계를 체계적으로 관리하고, 문제 해결을 용이하게 하기 위함입니다. |
| **OSI 모델에서 데이터 캡슐화(Encapsulation)와 역캡슐화(Decapsulation)는 무엇인가요?** | 캡슐화는 송신 측에서 데이터에 헤더를 추가하며 계층을 내려가는 과정이며, 역캡슐화는 수신 측에서 데이터를 원래 형태로 복원하며 계층을 올라가는 과정입니다. |
| **VPN(Virtual Private Network)은 OSI 7계층에서 어느 계층에서 동작하나요?** | VPN은 주로 네트워크 계층(3계층, IPsec) 또는 전송 계층(4계층, SSL/TLS VPN) 에서 동작하며, 보안 터널을 생성하여 안전한 데이터 전송을 보장합니다. |
| **OSI 7계층 모델을 적용한 실제 네트워크 데이터 흐름** | 사용자가 웹사이트에 접속하면, 데이터는 애플리케이션 계층(HTTP)에서 시작해 캡슐화되어 물리 계층까지 내려가고, 수신 측에서 역캡슐화되어 다시 애플리케이션 계층으로 전달됩니다. |