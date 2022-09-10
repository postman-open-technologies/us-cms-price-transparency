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
import json
import sqlite3
import asyncio
import aiohttp

# Create a SQLite table of URLs and filesizes
con = sqlite3.connect("./kaiser_data.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS in_network_files(url PRIMARY KEY UNIQUE, size)")

urls = []

# Get the list of in-network files from Kaiser's page
# Capture only the negotiated rates files (ignore table of contents and allowed amounts files)
resp = requests.get("https://healthy.kaiserpermanente.org/pricing/innetwork/2022-08_List.txt")
for line in resp.text.split("\n"):
    url = "https://healthy.kaiserpermanente.org/pricing/innetwork" + line.split("  ")[0].strip().replace(" ", "")
    print(url)
    if "in-network-rates" in url:
        urls.append(url)
    # Kaiser breaks the convention with their MRFs by not labeling them correctly here
    elif "KPWA_FILE" in url:
        urls.append(url)

async def fetch_url_sizes(table, urls):
    """
    Simple async function for getting all the file sizes in a list of urls
    and writing those to a SQLite table
    """
    
    session = aiohttp.ClientSession()
    fs = [session.head(url) for url in urls]

    for f in asyncio.as_completed(fs):
        resp = await f
        url = str(resp.url)
        size = int(resp.headers.get("content-length", -1))
        cur.execute(f"""INSERT OR IGNORE INTO {table} VALUES ("{url}", {size})""")
        con.commit()
        
    await session.close()

print("Fetching URLs and their sizes...")    
asyncio.run(fetch_url_sizes("in_network_files", urls))
total = cur.execute("SELECT SUM(size) FROM in_network_files").fetchone()[0]

print(f"Total filesize in GB: {total//1_000_000_000}")