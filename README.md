# Telegram Chatbot - OpenAI API

인공지능(openai의 API)을 사용하여 텔레그램 챗봇을 만드는 연습을 합니다.

Telegram API: <https://github.com/python-telegram-bot/python-telegram-bot/>

OpenAI API: <https://platform.openai.com/docs/api-reference/chat>

OpenAI API 연습하기 GitHub: <https://github.com/just-record/openai_api/tree/main>

코드는 **Branch별로** 구분되어 있습니다.

## 설치

```bash
pip install -r requirements.txt
```

`.env` 파일을 생성하고 아래 내용을 추가합니다.

```bash
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

`python file`을 실행합니다.

```bash
python main_ai_answer.py
```

## 01.pure_telegram_bot_api

제일 먼저 Pure Telegram Bot API를 사용하여 텔레그램 메시지를 받고 보내는 방법을 연습합니다.

## 02.my_first_chatbot

Telegram Bot API를 사용하여 간단한 챗봇을 만드는 방법을 연습합니다.

- Apllication 객체 생성
- 특정 명령어 처리 하기
- 메시지 보내면 동일한 메시지로 응답하기

## 03.telegram_chatbot_chatGPT

인공지능(OpenAI의 API)을 사용하여 자동으로 답변 하는 방법을 연습합니다.

- 자동 답변하기
- 영어로 번역하기
- 이미지 생성 하기
- 이미지를 업로드 하여 질의 하기

## TODO

- [ ] 이전 대화 기억하기
