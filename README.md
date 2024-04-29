# Telegram API - 첫 번째 Bot 만들기

Pure Telegram Bot API를 사용하기 연습

<https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot>

## `Application` Object

`build_application.py`: Application 객체를 생성합니다.

이 프로그램은 Application 객체를 생성하고 바로 종료합니다. 실제로 Application 객체만으로는 아무것도 할 수 없습니다.

## `/start` Command

`start_command.py`: `CommandHandler`를 이용 하여 `/start` 명령어를 처리합니다.

서비스를 종료 할 때 까지 계속 실행되며, 사용자가 `/start` 명령어를 입력하면 `"I'm a bot, please talk to me!"`를 답변합니다. 이 프로그램은 `/start` 명령어만 처리 할 수 있습니다.

## `Message`에 답변하기

`echo_bot.py`: `MessageHandler`를 이용하여 사용자가 입력한 메시지를 처리합니다.

사용자가 입력한 메시지를 그대로 답변합니다.

## 인자가 있는 `Command` 처리하기

`cap_bot.py`: `CommandHandler`를 이용하여 `/caps` 명령어를 처리합니다.

`/caps` 명령어 뒤에 입력한 문자열을 대문자로 변환하여 답변합니다.

**`InlineQueryHandler`** 은 다음에 연습할 예정입니다.
