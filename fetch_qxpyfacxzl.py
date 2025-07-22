import requests

cookie = input('Cookie: ')

headers = {
    'Cookie': cookie,
}

r = requests.get('https://byxt.buaa.edu.cn/jwapp/sys/qxfacx/modules/pyfacxepg/qxpyfacxzl.do', headers=headers)

with open('qxpyfacxzl.json', 'wb') as f:
    f.write(r.content)
