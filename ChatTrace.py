import json

with open('user_data_tiktok.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

chat_history = data.get("Direct Message", {}) \
                   .get("Direct Messages", {}) \
                   .get("ChatHistory", {})

your_username = "nama username kamu, tanpa @" 
target_username = "nama username target, tanpa @" 

sent = 0
received = 0

for key, messages in chat_history.items():
    if target_username in key:
        for msg in messages:
            sender = msg.get("From", "")
            if sender == your_username:
                sent += 1
            elif sender == target_username:
                received += 1

print(f"Kamu mengirim {sent} pesan ke @{target_username}")
print(f"Kamu menerima {received} pesan dari @{target_username}")
print(f"Total interaksi: {sent + received} pesan")
