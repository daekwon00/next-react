# 사용자 관리 시스템

Python 백엔드와 React 프론트엔드로 구성된 사용자 관리 시스템입니다.

## 프로젝트 구조

project-root/
├── backend/
│ ├── app.py # Flask 백엔드 애플리케이션
│ ├── User.py # 사용자 모델 및 CRUD 기능
│ └── requirements.txt
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ │ ├── UserDetail.js
│ │ │ └── UserForm.js
│ │ ├── App.js
│ │ └── App.css
│ └── package.json
├── package.json
└── README.md

## 기술 스택

- **백엔드**: Python, Flask
- **프론트엔드**: React, Axios
- **개발 도구**: Node.js, npm, concurrently

## 설치 방법

### 사전 요구사항

- Node.js 및 npm
- Python 3.x
- pip3

### 설치 단계

1. 저장소 클론

```bash
git clone <repository-url>
cd <project-directory>
```

2. 의존성 설치

```bash
# 루트 디렉토리에서 실행
npm install
npm run setup
```

또는 각 부분을 개별적으로 설치:

```bash
# 백엔드 의존성 설치
cd backend
pip3 install -r requirements.txt

# 프론트엔드 의존성 설치
cd frontend
npm install
```

## 실행 방법

### 개발 모드

```bash
# 루트 디렉토리에서 백엔드와 프론트엔드를 동시에 실행
npm run dev
```

또는 각 부분을 개별적으로 실행:

```bash
# 백엔드 실행
cd backend
python3 app.py

# 프론트엔드 실행
cd frontend
npm start
```

### 접속 방법

- 백엔드 API: http://localhost:5000
- 프론트엔드: http://localhost:3000

## API 엔드포인트

| 엔드포인트 | 메소드 | 설명 |
|------------|--------|------|
| `/api/users` | GET | 모든 사용자 목록 조회 |
| `/api/users/<user_id>` | GET | 특정 사용자 정보 조회 |
| `/api/users/<user_id>` | PUT | 사용자 정보 업데이트 |

## 기능

- 사용자 목록 조회
- 사용자 상세 정보 조회
- 사용자 정보 업데이트

## 개발자 정보

이 프로젝트는 Node.js를 사용하여 Python 백엔드와 React 프론트엔드를 통합한 예제 애플리케이션입니다. 