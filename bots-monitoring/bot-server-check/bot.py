import subprocess
import os
import requests

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

SCRIPT = "/usr/local/bin/maintenance.sh"


def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": message,
        },
        timeout=30,
    )


def main():

    result = subprocess.run(
        ["sudo", SCRIPT],
        capture_output=True,
        text=True
    )

    output = result.stdout

    message = f"""
🧹 SERVER MAINTENANCE
━━━━━━━━━━━━━━━━━━━━

{output}

━━━━━━━━━━━━━━━━━━━━
{"✅ Maintenance muvaffaqiyatli tugadi" if result.returncode == 0 else "❌ Maintenance xato bilan tugadi"}
"""

    send_telegram(message)


if __name__ == "__main__":
    main()
