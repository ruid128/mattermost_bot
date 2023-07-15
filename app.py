from flask import Flask, request
import requests
from openai_utils import *

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    # Получение текста сообщения пользователя
    message_text = data['text']
    channel_id = data['channel_id']

    # Обработка команд и формирование ответа
    response = process_message(message_text)

    # Отправка ответа в канал Mattermost
    send_message(channel_id, response)

    return 'OK'


def process_message(message_text):
    # Логика обработки сообщения пользователя и формирования ответа
    if message_text.startswith('/explain_code'):
        code = message_text[len('/explain_code'):].strip()
        explanation = get_code_explanation(code)
        return 'Explain: ' + explanation

    if message_text.startswith('/find_error'):
        code = message_text[len('/find_error'):].strip()
        error = find_code_error(code)
        return 'Error: ' + error

    if message_text.startswith('/shorten_text'):
        text = message_text[len('/shorten_text'):].strip()
        shortened_text = shorten_text(text)
        return 'Shortened text: ' + shortened_text

    if message_text.startswith('/paraphrase_text'):
        text = message_text[len('/paraphrase_text'):].strip()
        paraphrased_text = paraphrase_text(text)
        return 'Paraphrased text: ' + paraphrased_text

    if message_text.startswith('/optimize_query'):
        query = message_text[len('/optimize_query'):].strip()
        optimized_query = optimize_query(query)
        return 'Optimized query: ' + optimized_query

    # Если не найдена подходящая команда, возвращаем сообщение-подсказку
    return 'Доступные команды:\n/explain_code <code>\n/find_error <code>\n/shorten_text <text>\n/paraphrase_text <text>\n/optimize_query <query>'


def send_message(channel_id, message):
    mattermost_url = "MATTERMOST_API_URL"
    access_token = "MATTERMOST_ACCESS_TOKEN"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "channel_id": channel_id,
        "message": message
    }

    response = requests.post(f"{mattermost_url}/api/v4/posts", headers=headers, json=payload)

    if response.status_code == 201:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Error: {response.text}")


if __name__ == '__main__':
    app.run()
