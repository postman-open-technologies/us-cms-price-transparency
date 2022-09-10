"""
   Copyright 2022 Dolthub Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import requests
import sqlite3

con = sqlite3.connect("humana_data.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS in_network_files(url PRIMARY KEY UNIQUE, size)")

params = {
    "fileType": "innetwork",
    "iDisplayLength": "500000",
}

print("Fetching URLs and their sizes...")
resp = requests.get("https://developers.humana.com/Resource/GetData", params = params)

for file in resp.json()["aaData"]:
    url = "https://developers.humana.com/Resource/DownloadPCTFile?fileType=innetwork&" + file["name"]
    size = int(file["size"])
    cur.execute(f"""INSERT OR IGNORE INTO in_network_files VALUES ("{url}", {size})""")

con.commit()

total = cur.execute("SELECT SUM(size) FROM in_network_files").fetchone()[0]
print(f"Total filesize in GB: {total//1_000_000_000}")