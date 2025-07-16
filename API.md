# API

## 全校培养方案查询
```
POST https://byxt.buaa.edu.cn/jwapp/sys/qxfacx/modules/pyfacxepg/qxpyfacxzl.do
```

载荷：`application/x-www-form-urlencoded`

```
pageSize=50&pageNumber=1
```

响应：`application/json`

```json
{
    "datas": {
        "qxpyfacxzl": {
            "totalSize": 289,
            "pageNumber": 1,
            "pageSize": 50,
            "rows": [
                {
                    "SHR": "P00692",
                    "SHYJ": "同意",
                    "ZYDM": "0101",
                    "XLCCDM": null,
                    "ZYZYSY": null,
                    "XZNX": 4,
                    "PDFFJ": "2tcv28253g2t2v5l2pid336k3l4s3ctg721",
                    "DWDM": "01",
                    "XWDM": null,
                    "NJDM_DISPLAY": "2021级",
                    "PYMB": null,
                    "XDYQ": null,
                    "KSXQDM_DISPLAY": "秋季",
                    "ZSYQXF": 165.0,
                    "KSXNDM_DISPLAY": "2021-2022学年",
                    "ZYFXDM_DISPLAY": "",
                    "SLDM": "PYFASH",
                    "ZYDM_DISPLAY": "材料科学与工程",
                    "MBDM": null,
                    "SHSJ": "2024-05-08 16:25:51",
                    "SFFB": null,
                    "SHRXM": "王雨晴",
                    "CZRXM": "王雨晴",
                    "XQLXDM_DISPLAY": "秋春夏（一年三学期）",
                    "NJDM": "2021",
                    "ZSYQXFXSZ": 165.0,
                    "FAZTDM": "99",
                    "PYFADM": "2021_0101_01_",
                    "FJWID": "f047a8d15ebb4d9683e1a9228bf38236",
                    "ZGXK": null,
                    "XDLXDM_DISPLAY": "主修",
                    "WID": "1565A387B2F42C15E0630211FE0A7F20",
                    "PYFAMC": "2021级材料科学与工程主修培养方案",
                    "XDLXDM": "01",
                    "KSXQDM": "1",
                    "KSXNDM": "2021-2022",
                    "CZR": "P00692",
                    "BZ": null,
                    "PYCCDM": "01",
                    "FACCDM": null,
                    "ZGKC": null,
                    "CZSJ": "2024-09-05 14:14:35",
                    "CZIP": null,
                    "XQLXDM": "3",
                    "KZZD4": null,
                    "KZZD3": null,
                    "KZZD2": null,
                    "KZZD1": null,
                    "XWDM_DISPLAY": "",
                    "PYCCDM_DISPLAY": "本科",
                    "KZZD5": null,
                    "FATS": null,
                    "SHIP": null,
                    "DWDM_DISPLAY": "材料科学与工程学院",
                    "ZYFXDM": null
                },
                ...
            ]
        }
    },
    "code": "0"
}
```

## 获取附件
```
GET https://byxt.buaa.edu.cn/jwapp/sys/emapcomponent/file/getAttachmentFile/<FJWID>.do
```

`<FJWID>` 可通过[全校培养方案查询 API](#全校培养方案查询) 获取。

## 培养方案查询
```
POST https://byxt.buaa.edu.cn/jwapp/sys/jwpubapp/modules/pyfa/qxpyfacx.do
```

载荷：`application/x-www-form-urlencoded`

```
PYFADM=6cd5984f63b24ebaaeeaef1cfe04d7a7
```

响应：`application/json`

```json
{
    "datas": {
        "qxpyfacx": {
            "totalSize": 1,
            "pageSize": 999,
            "rows": [
                {
                    "SHR": "P00692",
                    "SFJCDLFA": null,
                    "SHYJ": "同意",
                    "ZYDM": "0601",
                    "XLCCDM": null,
                    "ZYZYSY": null,
                    "XZNX": 4,
                    "DWDM": "06",
                    "XWDM": null,
                    "NJDM_DISPLAY": "2022级",
                    "PYMB": "...",
                    "XDYQ": "...",
                    "DLXQ": null,
                    "KSXQDM_DISPLAY": "秋季",
                    "ZSYQXF": 169.0,
                    "KSXNDM_DISPLAY": "2022-2023学年",
                    "ZYFXDM_DISPLAY": "",
                    "SLDM": "PYFASH",
                    "ZYDM_DISPLAY": "计算机科学与技术",
                    "MBDM": null,
                    "SHSJ": "2025-04-23 09:18:02",
                    "SFFB": null,
                    "SHRXM": "王雨晴",
                    "CZRXM": "王雨晴",
                    "JCDLFADM": null,
                    "XQLXDM_DISPLAY": "秋春夏（一年三学期）",
                    "NJDM": "2022",
                    "ZSYQXFXSZ": 169.0,
                    "FAZTDM": "99",
                    "PYFADM": "6cd5984f63b24ebaaeeaef1cfe04d7a7",
                    "ZGXK": null,
                    "XDLXDM_DISPLAY": "主修",
                    "WID": "179A99035908AA09E0630111FE0AE6EF",
                    "PYFAMC": "2022级计算机科学与技术主修培养方案4",
                    "XDLXDM": "01",
                    "XGSM": null,
                    "KSXQDM": "1",
                    "KSXNDM": "2022-2023",
                    "CZR": "P00692",
                    "BZ": null,
                    "FACCDM": null,
                    "PYCCDM": "01",
                    "ZGKC": null,
                    "CZSJ": "2025-04-23 09:18:02",
                    "CZIP": null,
                    "XQLXDM": "3",
                    "KZZD4": null,
                    "KZZD3": null,
                    "KZZD2": null,
                    "KZZD1": null,
                    "XWDM_DISPLAY": "",
                    "KZZD5": null,
                    "FALXDM": "2",
                    "DWDM_DISPLAY": "计算机学院",
                    "FATS": null,
                    "SHIP": null,
                    "ZYFXDM": null
                }
            ],
            "extParams": {
                "logId": "a2d5e9bfd57f4efcb01c05614077e9ee",
                "code": 1,
                "totalPage": 0
            }
        }
    },
    "code": "0"
}
```

## 培养方案课程组查询
```
POST https://byxt.buaa.edu.cn/jwapp/sys/jwpubapp/modules/pyfa/kzcx.do
```

载荷：`application/x-www-form-urlencoded`

```
PYFADM=6cd5984f63b24ebaaeeaef1cfe04d7a7
```

响应：`application/json`

```json
{
    "datas": {
        "kzcx": {
            "totalSize": 41,
            "pageSize": 999,
            "rows": [
                {
                    "PYFADM": "6cd5984f63b24ebaaeeaef1cfe04d7a7",
                    "KCXZDM_DISPLAY": "",
                    "WID": "179A9903590CAA09E0630111FE0AE6EF",
                    "SFKK": null,
                    "KZLXDM_DISPLAY": "平台",
                    "ZDXDXF": null,
                    "BZ": null,
                    "SFXGXKZ": "0",
                    "KCZXS": null,
                    "ZYFXMC": null,
                    "KCXZDM": null,
                    "XDYQ": null,
                    "FKZH": "0b051185a32d48c598edbf48b9ebc53f",
                    "KCZXF": null,
                    "SFXGXKZ_DISPLAY": "否",
                    "KCLBDM_DISPLAY": "",
                    "SFKK_DISPLAY": "",
                    "ZYFXDM_DISPLAY": "",
                    "KZH": "5ea69c848f7e47b78a5b6008286d32e3",
                    "GGKZH": null,
                    "ZSXDXF": 22.0,
                    "KZLXDM": "02",
                    "ZSXDMS": null,
                    "XGXKLBDM": null,
                    "KZM": "1.1 北航学院数学类",
                    "KCLBDM": null,
                    "ZYFXDM": null,
                    "PX": 1.0,
                    "ZSWCKZS": null,
                    "KCZMS": null
                },
                ...
            ],
            "extParams": {
                "logId": "006e4c861a604aee9e022a61618f9b7f",
                "code": 1,
                "totalPage": 0
            }
        }
    },
    "code": "0"
}
```

## 培养方案课程查询
```
POST https://byxt.buaa.edu.cn/jwapp/sys/jwpubapp/modules/pyfa/kzkccx.do
```

载荷：`application/x-www-form-urlencoded`

```
PYFADM=6cd5984f63b24ebaaeeaef1cfe04d7a7
```

响应：`application/json`

```json
{
    "datas": {
        "kzkccx": {
            "totalSize": 586,
            "pageSize": 999,
            "rows": [
                {
                    "PYFADM": "6cd5984f63b24ebaaeeaef1cfe04d7a7",
                    "XS": 30.0,
                    "KCXZDM_DISPLAY": "必修",
                    "WID": "eb67a120fb7f415a8b0f253215572ade",
                    "XNXQ_DISPLAY": "",
                    "FXXS14": null,
                    "BZ": null,
                    "XXKC": null,
                    "SFZGKC": null,
                    "FXXS10": null,
                    "XF": "1.5",
                    "FXXS11": null,
                    "KSLXDM_DISPLAY": "考试",
                    "JHXNDM": null,
                    "FXXS12": null,
                    "FXXS13": null,
                    "KCXZDM": "01",
                    "JYSDM": null,
                    "XDXQ": null,
                    "SFZGKC_DISPLAY": "",
                    "XDXNXQ": null,
                    "CDDWDM_DISPLAY": "",
                    "KSLXDM": "02",
                    "JHXQDM": null,
                    "KZH": "687cd8103c2f4b768ff01c485408a428",
                    "FXXS06": null,
                    "FXXS05": null,
                    "FXXS04": null,
                    "FXXS03": null,
                    "FXXS09": null,
                    "FXXS08": null,
                    "KZM": "美育课",
                    "FXXS07": null,
                    "CDDWDM": null,
                    "FXXS01": null,
                    "XNXQ": null,
                    "FXXS02": null,
                    "JYSDM_DISPLAY": "",
                    "CXXQ": null,
                    "KCM": "西方音乐史与名曲鉴赏",
                    "PX": null,
                    "KCH": "50G01050"
                },
                ...
            ],
            "extParams": {
                "logId": "90fd62920af949259e95c3959d1ba7a2",
                "code": 1,
                "totalPage": 0
            }
        }
    },
    "code": "0"
}
```

## 培养方案附加指标查询
```
POST https://byxt.buaa.edu.cn/jwapp/sys/jwpubapp/modules/pyfa/gjpyfadmczfazbms.do
```

载荷：`application/x-www-form-urlencoded`

```
PYFADM=6cd5984f63b24ebaaeeaef1cfe04d7a7
```

响应：`application/json`

```json
{
    "datas": {
        "gjpyfadmczfazbms": {
            "totalSize": 1,
            "pageSize": 5000,
            "rows": [
                {
                    "ZBYQGXMS": "32.0\u003c=劳育学时\u003c=999.0 且 3.0\u003c=创新创业学分要求\u003c=99.0 且 2.0\u003c=全英文课程要求\u003c=99.0 且 1.5\u003c=美育学分指标\u003c=99.0 且 1.0\u003c=人文、经典、社科、科技文明 4 类\u003c=99.0"
                }
            ]
        }
    },
    "code": "0"
}
```
