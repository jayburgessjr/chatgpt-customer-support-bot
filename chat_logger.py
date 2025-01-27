import os
from datetime import datetime

def log_chat(user_input, bot_response, language):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"chat_log_{datetime.now().date()}.txt")

    with open(log_file, "a") as f:
        f.write(f"[{datetime.now()}] Language: {language}\n")
        f.write(f"User: {user_input}\n")
        f.write(f"Bot: {bot_response}\n")
        f.write("---\n")
