# Telegram Chatbot - openai의 API 연동

인공지능(openai의 API)을 사용하여 텔레그램 챗봇을 만드는 연습을 합니다.

Telegram API: <https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot>

OpenAI API: <https://platform.openai.com/docs/api-reference/chat>

## OpenAI API

OpenAI API의 기능: <https://github.com/just-record/openai_api>

`.env` 파일에 API 키를 저장합니다.

```shell
OPENAI_API_KEY=your_api_key
```

## 답변 생성

`main_ai_answer.py`: AI를 활용하여 채팅 메시지에 답변을 합니다. 이전 대화를 기억 하지는 못합니다.

## 답변 기능 추가

`main_ai_english.py`: 채팅 메시지를 영어로 번역합니다.

OpenAI API의 System content를 사용하여 답변에 특정 기능을 부여합니다.

## 이미지 생성

`main_ai_image.py`: OpenAI API의 이미지 생성 기능을 사용하여 이미지를 생성합니다.
