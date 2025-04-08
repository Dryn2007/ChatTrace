import json
from collections import Counter
from datetime import datetime

# Load data dari file
with open('user_data_tiktok.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

chat_history = data.get("Direct Message", {}) \
                   .get("Direct Messages", {}) \
                   .get("ChatHistory", {})

your_username = "username kamu"
target_username = "username target"

sent = 0
received = 0
hour_counter = Counter()
start_counter = {your_username: 0, target_username: 0}
ghosting_counter = {your_username: 0, target_username: 0}

# Proses semua chat history
for key, messages in chat_history.items():
    if target_username in key:
        # Hitung jumlah kirim/terima
        for msg in messages:
            sender = msg.get("From", "")
            if sender == your_username:
                sent += 1
            elif sender == target_username:
                received += 1

        # Urutkan berdasarkan waktu
        messages = sorted(messages, key=lambda m: m.get("Date", ""))
        last_sender = None

        for i, msg in enumerate(messages):
            sender = msg.get("From", "")
            date_str = msg.get("Date", "")

            # Ambil jam dari Date
            try:
                dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                hour_counter[dt.hour] += 1
            except:
                continue

# 💬 Output jumlah kirim/terima pesan
print(f"\n📨 Interaksi antara kamu dan @{target_username}:")
print(f"- Kamu mengirim {sent} pesan ke {target_username}")
print(f"- Kamu menerima {received} pesan dari {target_username}")
print(f"- Total interaksi: {sent + received} pesan")

# ⏰ Output jam ngobrol
print("\n🕒 Jam paling aktif ngobrol:")
for hour, count in hour_counter.most_common():
    print(f"- Jam {hour:02d}:00 — {count} pesan")

# 👻 Ghosting counter
print("\n👻 Ghosting checker:")
print(f"- Pesan kamu yg gak dibales: {ghosting_counter[your_username]} kali")
print(f"- Pesan dia yg gak kamu bales: {ghosting_counter[target_username]} kali")
