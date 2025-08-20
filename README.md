# Gemini 이미지 생성기 MCP 서버 (수정 버전)

Claude Desktop에서 Google의 Gemini AI를 사용하여 고품질 이미지를 생성하고 편집할 수 있는 MCP 서버입니다.

## 🚀 주요 특징

- **텍스트로 이미지 생성**: Gemini 2.0 Flash를 사용한 텍스트-이미지 변환
- **이미지 변환**: 기존 이미지를 텍스트 프롬프트로 수정
- **한글 지원**: 한글 프롬프트 자동 번역 및 최적화
- **지능형 파일명 생성**: AI가 프롬프트 기반으로 파일명 자동 생성
- **로컬 저장**: 생성된 이미지를 지정한 폴더에 자동 저장

## 🛠️ 설치 요구사항

- **Python 3.11 이상**
- **Google Gemini API 키**
- **Claude Desktop** 또는 기타 MCP 호환 클라이언트

## 📋 1단계: Gemini API 키 발급

1. [Google AI Studio API Keys 페이지](https://aistudio.google.com/apikey) 접속
2. Google 계정으로 로그인
3. **"Create API Key"** 클릭
4. 생성된 API 키 복사 (나중에 사용)

## 💾 2단계: MCP 서버 설치

### 자동 설치 (권장)
```bash
# 저장소 클론
git clone https://github.com/my13each/mcp-server-gemini-image-generator-fixed.git
cd mcp-server-gemini-image-generator-fixed

# 가상환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -e .
```

### 설치 확인
```bash
# 서버가 정상 실행되는지 테스트
python -m mcp_server_gemini_image_generator.server
```
`Starting Gemini Image Generator MCP server...` 메시지가 나오면 성공! (Ctrl+C로 종료)

## ⚙️ 3단계: Claude Desktop 설정

### 설정 파일 위치
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

### 설정 파일 내용
```json
{
  "mcpServers": {
    "gemini-image-generator": {
      "command": "/절대경로/mcp-server-gemini-image-generator-fixed/venv/bin/python",
      "args": [
        "-m", "mcp_server_gemini_image_generator.server"
      ],
      "env": {
        "GEMINI_API_KEY": "여기에_실제_API키_입력",
        "OUTPUT_IMAGE_PATH": "/Users/사용자명/Pictures/ai_generated"
      }
    }
  }
}
```

### 실제 설정 예시
```json
{
  "mcpServers": {
    "gemini-image-generator": {
      "command": "/Users/jp17463/mcp-server-gemini-image-generator-fixed/venv/bin/python",
      "args": [
        "-m", "mcp_server_gemini_image_generator.server"
      ],
      "env": {
        "GEMINI_API_KEY": "AIzaSy...(실제_API키)",
        "OUTPUT_IMAGE_PATH": "/Users/jp17463/Pictures/ai_generated"
      }
    }
  }
}
```

### 🚨 중요사항
1. **절대 경로 사용**: 모든 경로는 전체 경로로 입력
2. **API 키 교체**: `여기에_실제_API키_입력` 부분을 발급받은 실제 키로 교체
3. **이미지 폴더**: `OUTPUT_IMAGE_PATH`에 지정한 폴더가 미리 생성되어 있어야 함

### 이미지 저장 폴더 생성
```bash
mkdir -p ~/Pictures/ai_generated
```

## 🎯 4단계: 실행 및 테스트

1. **Claude Desktop 재시작**: 설정 후 완전히 종료하고 다시 시작
2. **연결 확인**: Claude Desktop에서 MCP 서버가 연결되었는지 확인
3. **테스트**: "고양이 그림을 그려줘"라고 요청해보기

## 📖 사용법

### 이미지 생성
```
아름다운 후지산과 벚꽃이 있는 일본 풍경을 그려줘
```

### 이미지 변환 (파일 경로)
```
/Users/username/image.jpg 이 이미지에 무지개를 추가해줘
```

### 이미지 변환 (업로드)
이미지를 Claude에 업로드한 후:
```
이 이미지를 밤 풍경으로 바꿔줘
```

## 🔧 문제 해결

### 서버 연결 실패
1. **로그 확인**: Claude Desktop의 로그 폴더에서 `gemini-image-generator.log` 확인
2. **경로 확인**: `claude_desktop_config.json`의 Python 경로가 정확한지 확인
3. **권한 확인**: 이미지 저장 폴더에 쓰기 권한이 있는지 확인

### API 키 오류
1. **키 유효성**: Google AI Studio에서 API 키가 활성화되었는지 확인
2. **따옴표 확인**: 설정 파일에서 API 키가 따옴표로 감싸져 있는지 확인

### 수동 테스트
```bash
cd ~/mcp-server-gemini-image-generator-fixed
source venv/bin/activate
export GEMINI_API_KEY="실제_API키"
export OUTPUT_IMAGE_PATH="~/Pictures/ai_generated"
python -m mcp_server_gemini_image_generator.server
```

## 📊 제공되는 도구

### 1. `generate_image_from_text`
- **기능**: 텍스트 프롬프트로 새 이미지 생성
- **입력**: 이미지 설명 텍스트
- **출력**: 생성된 이미지 파일 경로

### 2. `transform_image_from_file`
- **기능**: 파일 경로의 이미지를 텍스트 프롬프트로 변환
- **입력**: 이미지 파일 경로, 변환 프롬프트
- **출력**: 변환된 이미지 파일 경로

### 3. `transform_image_from_encoded`
- **기능**: Base64 인코딩된 이미지를 텍스트 프롬프트로 변환
- **입력**: Base64 이미지 데이터, 변환 프롬프트
- **출력**: 변환된 이미지 파일 경로

## 📝 원본과의 차이점

이 수정 버전은 원본 저장소의 다음 문제들을 해결했습니다:

- ❌ **원본 문제**: JSON 직렬화 오류 (`invalid utf-8 sequence`)
- ❌ **원본 문제**: MCP 도구가 바이너리 데이터 반환으로 인한 실행 실패
- ✅ **수정 사항**: 파일 경로만 반환하여 안정적인 동작
- ✅ **수정 사항**: Claude Desktop에서 완벽하게 작동

## 🤝 기여 및 문의

- **원본 저장소**: [qhdrl12/mcp-server-gemini-image-generator](https://github.com/qhdrl12/mcp-server-gemini-image-generator)
- **수정 버전**: [my13each/mcp-server-gemini-image-generator-fixed](https://github.com/my13each/mcp-server-gemini-image-generator-fixed)
- **이슈 제보**: GitHub Issues 탭에서 문제 신고

## 📄 라이선스

MIT License - 원본 프로젝트와 동일

---

**팁**: 처음 설정할 때는 단계별로 차근차근 진행하시고, 문제가 생기면 로그 파일을 먼저 확인해보세요! 🚀