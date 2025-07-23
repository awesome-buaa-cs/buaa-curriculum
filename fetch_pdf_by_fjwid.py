import json
import os
import re
import requests
import time
import urllib.parse

os.mkdir('PDF-By-FJWID')

with open('qxpyfacxzl.json', 'r') as f:
    qxpyfacxzl = json.load(f)

rows = qxpyfacxzl['datas']['qxpyfacxzl']['rows']

cookie = input('Cookie: ')

headers = {
    'Cookie': cookie,
}

for index, row in enumerate(rows):
    print(f'Downloading {index + 1} / {len(rows)}')

    fjwid = row['FJWID']
    r = requests.get(
        f'https://byxt.buaa.edu.cn/jwapp/sys/emapcomponent/file/getAttachmentFile/{fjwid}.do',
        headers=headers,
    )

    # Content-Disposition: attachment; filename="<encoded-filename>.pdf"
    content_disposition = r.headers.get('Content-Disposition')
    m = re.fullmatch(
        r'''attachment; filename="[^"]+"; filename\*=utf-8''(.+)''',
        content_disposition,
    )
    filename = urllib.parse.unquote(m.group(1))
    dirpath = f'PDF-By-FJWID/{fjwid}'
    filepath = f'PDF-By-FJWID/{fjwid}/{filename}'

    if os.path.exists(dirpath):
        print(f'Duplicate FJWID: {fjwid}, skipping.')
        continue
    os.mkdir(dirpath)
    with open(filepath, 'wb') as file:
        file.write(r.content)

    time.sleep(3)
