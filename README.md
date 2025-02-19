# DiscordWorkLogger

DiscordWorkLogger は、Discord Bot を使用して出勤・退勤メッセージを Google Apps Script (GAS) を介して Google スプレッドシートに記録するプロジェクトです。

## 機能

1. Discord の指定チャンネルでユーザーが「おはよう」や「お疲れ」と発言すると、GAS を通じてスプレッドシートに出勤・退勤時間を記録します。
2. 各ユーザーに対応する GAS の URL を設定し、個別のスプレッドシートを操作できます。
3. 記録に成功すると、Discord メッセージにリアクションを付けてユーザーに通知します。

---

## 必要なツールとライブラリ

- [Python](https://www.python.org/) 3.x
- [Discord.py](https://discordpy.readthedocs.io/) ライブラリ
- [Google Apps Script](https://developers.google.com/apps-script)
- `.env` ファイル（環境変数の設定用）

---

## Google Apps Script (GAS) のデプロイ方法

**[わかりやすいデプロイ方法](https://coffee-soldier-56f.notion.site/gas-188729a7cf0380e89c74ca1d8d68d66d)**はこちら

<!-- 1. **GAS プロジェクトを作成**
   - Google ドライブで新しいスクリプトプロジェクトを作成します。

2. **スクリプトをコピー**
   - このリポジトリ内の `gas_script.js` をコピーして貼り付けます。

3. **Web App をデプロイ**
   - `公開 > ウェブアプリケーションとして導入` を選択。
   - 「アプリケーションにアクセスできるユーザー」を「全員（匿名ユーザーを含む）」に設定。

4. **スプレッドシートのフォーマット**
   スプレッドシートの各列は以下のように構成されます：

   | B列   | C列 | D列 | E列   | F列   | G列       |H列       |I列       |
   | ---- | ------ | --- | --- | ----- | ----- | --------- |--------- |
   | 日付 | 曜日   | ステータス | 出勤時間  | 退勤時間 | 休憩時間 | 実働時間 | 備考 | -->

---

## Discord Bot の設定

### Discord Bot の権限について

- **必要な権限**

   - OAuth2
       - OAuth2 URL Generator
           - Scopes: `bot`
           - Bot Permissions: `View Channels`, `Add Reactions`

   - Bot
       - Privileged Gateway Intents
           - `Presence Intent`, `Server Members Intent`, `Message Content Intent`を有効化

---

## 環境設定

1. **Discord Bot のトークンを取得**
   - Discord Developer Portal にて Bot を作成し、トークンを取得します。

2. **.env ファイルを作成**
   プロジェクトのルートディレクトリに `.env` ファイルを作成し、以下のように環境変数を設定します：

   ```env
   DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
   TARGET_GUILD_ID=YOUR_GUILD_ID
   TARGET_CHANNEL_ID=YOUR_CHANNEL_ID
   ```

3. **ユーザー ID と GAS URL のマッピング**
   - `user_gas_mapping.json` ファイルを作成し、以下のようにユーザー ID と GAS の Web App URL をマッピングします：

     ```json
     {
       "123456789012345678": "https://script.google.com/macros/s/abc1234567890/exec",
       "876543210987654321": "https://script.google.com/macros/s/def0987654321/exec"
     }
     ```

---

## 使用方法

### DockerでDiscord Bot の起動(推奨)

1. **Docker イメージをビルド**

   ```bash
   docker compose build
   ```

2. **Docker コンテナを起動**

   ```bash
    docker compose up -d
    ```

### Discord Bot の起動(非推奨)

1. **Python スクリプトを実行**

   ```bash
   python main.py
   ```

2. **Discord チャンネルで出勤・退勤メッセージを送信**
   - 出勤メッセージ: 「おはよう」
       - 出社メッセージ: 「出社」
   - 退勤メッセージ: 「お疲れ」

3. **リアクションで結果を確認**
   - ✅: 記録成功
   - ❌: 記録失敗
   - ❓: GAS URL が設定されていない

---

## ファイル構成

```tree
DiscordWorkLogger/
├── main.py                 # Discord Bot のメインスクリプト
├── gas_script.js          # Google Apps Script
├── user_gas_mapping.json  # ユーザー ID と GAS URL のマッピング
├── .env                   # 環境変数ファイル
└── README.md              # 説明書
```

---

## 注意点

- GAS をデプロイする際は、スプレッドシートへのアクセス権限を適切に設定してください。
- Discord Bot を稼働させる環境に Python と必要なライブラリがインストールされていることを確認してください。

---

This README is generated by AI. 🤖
