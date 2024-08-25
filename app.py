import streamlit as st

from google.oauth2.service_account import Credentials
import gspread

st.write("TEST")

# スコープを指定
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# サービスアカウントのJSONファイルを使用して認証情報を作成
service_account_info = st.secrets["gcp_service_account"]

# 認証情報を作成
creds = Credentials.from_service_account_info(service_account_info, scopes=scopes)

# gspreadクライアントを作成
client = gspread.authorize(creds)

# スプレッドシートの取得
spreadsheet_id = '14PmuhBLAv54cUmYeQfo2BqwJHe8FQWUIaZAoJry78So'  # スプレッドシートIDを設定
spreadsheet = client.open_by_key(spreadsheet_id)

# ワークシートの取得
worksheet = spreadsheet.sheet1  # 最初のワークシートを取得
data = worksheet.get_all_records()  # データを取得
st.write(data)
