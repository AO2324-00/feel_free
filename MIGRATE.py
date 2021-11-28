import sqlite3


# データベース名
dbname = 'FeelFree.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# 場所
cur.execute("DROP TABLE IF EXISTS places")
cur.execute("CREATE TABLE places(id INTEGER PRIMARY KEY, title TEXT NOT NULL, address TEXT NOT NULL, image_url TEXT NOT NULL, created_at  DATETIME DEFAULT CURRENT_TIMESTAMP)")

# 貸し出し履歴
cur.execute("DROP TABLE IF EXISTS lend")
cur.execute("CREATE TABLE lend(id INTEGER PRIMARY KEY, place_id INT NOT NULL,  begin_date DATETIME NOT NULL, end_date DATETIME NOT NULL, purpose TEXT)")

# 初期データの挿入
cur.execute('INSERT INTO places(title, address, image_url) VALUES("ABCスペース", "○○県○○市○○", "https://msp.c.yimg.jp/images/v2/FUTi93tXq405grZVGgDqGxaYEnV9QZCgT1neehchCxqKUH4ufWBnDGZKCOUwmFgayRdesg4qpGQf3XvX_DBKpHCqWX2gSeHoWrsSR_PB1rxvAaYccsUuTml1YVcFZOIp99JZeiXXVD3dIJFOVzPdWE6sTsCFiRSsOby1y3wCDqLQcyxJIRW0TTlfiJDP-sNfuYUB9pYy_2-KWmwZtUUQQNIe1xPbOCRb0CCjl2tzkZ2DZNRaifXhNCs_BugWVA5o/Octocat.png?errorImage=false")')
cur.execute("INSERT INTO lend (place_id, begin_date, end_date, purpose) VALUES (:place_id, :begin_date, :end_date, :purpose)", (1, "2021-11-28 10:52:16", "2021-11-29 10:52:16", "利用目的"))
conn.commit()

# 初期データの確認
cur.execute("SELECT * FROM places")
for row in cur:
    print("id: " + str(row[0]) + ", title: " + str(row[1]) + ", address: " + str(row[2]) + ", image_url: " + str(row[3]) + ", created_at: " + str(row[4]) )

cur.execute("SELECT * FROM lend")
print(cur.fetchone())

# データベースへのコネクションを閉じる。(必須)
conn.close()

