import requests
import os

def send_line_notification(message):
    line_token = os.environ.get("LINE_NOTIFY_TOKEN")
    headers = {'Authorization': 'Bearer ' + line_token}
    payload = {'message': message}
    response = requests.post('https://notify-api.line.me/api/notify', headers=headers, data=payload)
    return response

if __name__ == "__main__":
    send_line_notification("5分ごとの定期実行: GitHub Actions workflow completed!")