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
cur.execute("CREATE TABLE lend(id INTEGER PRIMARY KEY, place_id INT NOT NULL,  begin_date DATETIME NOT NULL, end_date DATETIME NOT NULL, purpose TEXT NOT NULL, description TEXT DEFAULT '', event_url TEXT DEFAULT '')")

# デモデータの挿入
## 場所
cur.execute('INSERT INTO places(title, address, image_url) VALUES("長谷オフィス", "静岡県静岡市葵区長谷町32番地13号", "https://cdn.pixabay.com/photo/2016/11/07/19/25/meeting-room-1806702_960_720.jpg")')
cur.execute('INSERT INTO places(title, address, image_url) VALUES("早日渡ビル", "宮崎県延岡市北方町早日渡25番地5号", "https://cdn.pixabay.com/photo/2015/04/20/06/43/meeting-room-730679_960_720.jpg")')
cur.execute('INSERT INTO places(title, address, image_url) VALUES("堀ノ内オフィス", "神奈川県横浜市南区堀ノ内町2丁目109番地2号", "https://cdn.pixabay.com/photo/2017/08/06/11/09/interior-2591367_960_720.jpg")')
cur.execute('INSERT INTO places(title, address, image_url) VALUES("渋温泉 金具屋", "長野県下高井郡山ノ内町平穏２２０２", "https://siasky.net/AACK6GSbc2c4XhH4ucl1cu1acA5xmoY3I3M_YzOgQFzWqQ")')
cur.execute('INSERT INTO places(title, address, image_url) VALUES("白川郷", "岐阜県白川村, 大野郡,萩町", "https://siasky.net/vACKoT2zpj8gI3H-HKvD6k-nTQtztlebNLAiAYmPH-cMZw")')
cur.execute('INSERT INTO places(title, address, image_url) VALUES("場所9", "静岡県牧之原市坂部719番地18号", "https://4.bp.blogspot.com/-8tDg7zSeK2M/Wb8gHWCRfLI/AAAAAAABGvQ/Ju4XHm7iWh4APgEBirY-LgMKqq7i1m8RgCLcBGAs/s800/business_icon_big_company.png")')
cur.execute('INSERT INTO places(title, address, image_url) VALUES("場所10", "栃木県那須塩原市大原間86番地2号", "https://2.bp.blogspot.com/-rD3H2VLmAfk/VtoxsY5FYZI/AAAAAAAA4dM/0zz8r1VyCe4/s800/building_kaisya_small_blank.png")')
cur.execute('INSERT INTO places(title, address, image_url) VALUES("場所11", "島根県邑智郡邑南町上田所217番地4号", "https://2.bp.blogspot.com/-lCDK3KOboS8/WeAFbjwCLjI/AAAAAAABHjU/guFvIX2h73s5IPmZQ1Atk8kG58iaexiOACLcBGAs/s450/building_high2.png")')
cur.execute('INSERT INTO places(title, address, image_url) VALUES("場所12", "和歌山県有田郡有田川町中原962番地15号", "https://3.bp.blogspot.com/-Lcumj5myAeU/WlGpKowYfaI/AAAAAAABJk8/ENsUUTeurpY-pV_GAqVi4wc84V52l-KegCLcBGAs/s800/building_business_office.png")')
## 予約
cur.execute("INSERT INTO lend (place_id, begin_date, end_date, purpose, description, event_url) VALUES (:place_id, :begin_date, :end_date, :purpose, :description, :event_url)", (1, "2021-11-28 10:52:16", "2021-11-29 10:52:16", "利用目的", "詳細説明", "http://example.event.com"))
conn.commit()

# 初期データの確認
cur.execute("SELECT * FROM places")
for row in cur:
    print("id: " + str(row[0]) + ", title: " + str(row[1]) + ", address: " + str(row[2]) + ", image_url: " + str(row[3]) + ", created_at: " + str(row[4]) )

cur.execute("SELECT * FROM lend")
print(cur.fetchone())

# データベースへのコネクションを閉じる。(必須)
conn.close()

