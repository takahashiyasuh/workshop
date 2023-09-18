# ライブラリのインポート
import mysql.connector

# DB情報
DB_HOST='127.0.0.1'
DB_USER='root'
DB_PASSWORD='password'
DB_NAME='sales'

conn = None
curs = None

# DBコネクション
conn = mysql.connector.connect(host=DB_HOST,
                            user=DB_USER,
                            password=DB_PASSWORD,
                            database=DB_NAME)
# カーソル取得
curs = conn.cursor()

# データを取得
sql = 'SELECT id, goods, price, buy_date FROM sales;'
curs.execute(sql)
# fetchall()は中身を全て取得するメソッド
rows = curs.fetchall()

# 取得したデータをデバッグ表示
for id, goods, price, buy_date in rows:
    print(id, goods, price, buy_date)

# 終了処理
if curs is not None:
    curs.close()
if conn is not None:
    conn.close()
