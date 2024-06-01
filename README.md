# Telegram Chatbot - openai의 API 연동

인공지능(openai의 API)을 사용하여 텔레그램 챗봇을 만드는 연습을 합니다.

Telegram API: <https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot>

OpenAI API: <https://platform.openai.com/docs/api-reference/chat>

## OpenAI API

OpenAI API 연습하기: <https://github.com/just-record/openai_api>

`.env` 파일에 API 키를 저장합니다.

```shell
OPENAI_API_KEY=your_api_key
```

## 답변 생성

OpenAI API를 활용하여 채팅 메시지에 답변을 합니다. 이전 대화를 기억 하지는 못합니다.

`main_ai_answer.py`

## 답변 기능 추가

OpenAI API를 활용하여 채팅 메시지를 영어로 번역합니다.

- `main_ai_english.py`: Message Handler 사용 - 메시지를 무조건 영어로 번역합니다.
- `main_ai_english_command.py`: Command Handler 사용 - `/translation` 명령어를 사용하여 번역합니다.
  - `/translation 안녕하세요` 로 입력하면 영어로 번역합니다. 일반 메시지는 일반적인 답변을 합니다.

## 이미지 생성

OpenAI API를 활용하여 이미지를 생성합니다.

- `main_ai_image.py`: Message Handler 사용 - 메시지에 해당하는 이미지를 무조건 생성합니다.
- `main_ai_image_command.py`: Command Handler 사용 - `/generate_image` 명령어를 사용하여 이미지를 생성합니다.
  - `/generate_image cat` 로 입력하면 고양이 이미지를 생성합니다. 일반 메시지는 일반적인 답변을 합니다.

## 이미지를 업로드하고 질의 하기

OpenAI API를 활용하여 이미지와 그에 관한 질의를 합니다.

- `main_ai_image_query.py`: Message Handler 사용 - 업로드 하는 이미지의 caption에 입력한 내용을 질의 합니다.
