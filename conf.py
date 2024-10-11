from json import load
from json.decoder import JSONDecodeError

checklt = {
    'abort': [False,bool],
    'pause': [True,bool]
}

def confDefault():
    confD = {}
    for m,n in checklt.items():
        confD[m] = n[0]
    return confD

def confCheck(confG):
    confC = {}
    for m,n in confG.items():
        if checklt.get(m) == None:
            print('警告：{} 键是一个无效键。'.format(m))
        elif checklt.get(m)[1] != type(n):
            print('警告：{} 键的对应值不合法。'.format(m))
        else:
            confC[m] = n
    return confC

def confMerge(confD,confC):
    confD.update(confC)
    return confD

def confGet():
    try:
        with open('sync.json','r') as confR:
            confG = load(confR)
        print('配置文件读取成功！')
    except FileNotFoundError:
        print('配置文件不存在，将使用默认配置...')
        return confDefault()
    except JSONDecodeError:
        print('配置文件不合 JSON 语法，将使用默认配置...')
        return confDefault()
    return confMerge(confDefault(),confCheck(confG))
