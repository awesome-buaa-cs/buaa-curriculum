import json
import os
import shutil

os.mkdir('PDF-By-Year')

with open('qxpyfacxzl.json', 'r') as f:
    qxpyfacxzl = json.load(f)

rows = qxpyfacxzl['datas']['qxpyfacxzl']['rows']

for row in rows:
    fjwid = row['FJWID']
    njdm = row['NJDM']

    oldfilenames = os.listdir(f'PDF-By-FJWID/{fjwid}')
    assert len(oldfilenames) == 1
    oldfilename = oldfilenames[0]

    newdirpath = f'PDF-By-Year/{njdm}'
    os.makedirs(newdirpath, exist_ok=True)
    if os.path.exists(f'{newdirpath}/{oldfilename}'):
        print(f'Duplicate file name: {oldfilename}, skipping.')
        continue
    shutil.copy(f'PDF-By-FJWID/{fjwid}/{oldfilename}', newdirpath)
