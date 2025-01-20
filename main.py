import os
import discord
import requests
import json
# from dotenv import load_dotenv

# # .env ファイルから環境変数を読み込む
# load_dotenv()

# Discord ボットのトークンを取得
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# 対象のギルドとチャンネルの ID
TARGET_GUILD_ID = int(os.getenv('TARGET_GUILD_ID'))  # ギルド ID
TARGET_CHANNEL_ID = int(os.getenv('TARGET_CHANNEL_ID'))  # チャンネル ID

# ユーザー ID と GAS_URL のマッピングをロード
with open("user_gas_mapping.json", "r") as f:
    USER_GAS_MAPPING = json.load(f)

# Intents を設定
intents = discord.Intents.default()
intents.messages = True  # メッセージを取得する
intents.message_content = True  # メッセージ内容を取得する

# クライアントを作成
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    # 起動時
    print(f'Logged in as {client.user}!')

@client.event
async def on_message(message):
    # ボットのメッセージを無視
    if message.author.bot:
        return

    # メッセージが送信されたギルドが対象外の場合
    if message.guild.id != TARGET_GUILD_ID:
        return

    # 対象チャンネルか確認
    if message.channel.id != TARGET_CHANNEL_ID:
        return

    # ユーザー ID に基づいて GAS_URL を取得
    user_id = str(message.author.id)  # ユーザー ID を文字列に変換
    gas_url = USER_GAS_MAPPING.get(user_id)

    # GAS_URL が見つからない場合はスキップ
    if not gas_url:
        print(f"ユーザー ID {user_id} に対応する GAS_URL が見つかりません。")
        await message.add_reaction("❓")  # ❓
        return

    # メッセージ内容に応じてアクションを設定
    data = None
    if "おはよう" in message.content:
        data = {"action": "oha"}
    elif "お疲れ" in message.content:
        data = {"action": "otu"}

    # データが設定されていない場合は終了
    if not data:
        return

    # Google Apps Script を実行
    try:
        response = requests.post(gas_url, json=data)
        if response.status_code == 200:
            await message.add_reaction("✅")  # :white_check_mark:
        elif response.status_code == 404:
            print(f"err: {response.status_code}")
            await message.add_reaction("4️⃣")  # :x:
            await message.add_reaction("0️⃣")  # :x:
        else:
            print(f"err: {response.status_code}")
            await message.add_reaction("❌")  # :x:
    except Exception as e:
        print(f"err: {e}")
        await message.add_reaction("❌")  # :x:

# ボットを起動
if DISCORD_TOKEN:
    client.run(DISCORD_TOKEN)
else:
    print("DISCORD_TOKEN が .env ファイルに設定されていません。")
