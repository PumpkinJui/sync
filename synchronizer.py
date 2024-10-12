# https://blog.csdn.net/xy3233/article/details/122405558

from conf import confGet
from datetime import datetime
from ntplib import NTPClient
from os import system

conf = confGet()

print('当前本地时间：{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

ntpc = NTPClient()
received = False
writeBAT = True

for i in range(len(conf['servers'])):
    try:
        resp = ntpc.request(conf['servers'][i]).tx_time
        print('收到 NTP 服务器 {} 回复，当前时间戳为 {}'.format(conf['servers'][i],resp))
        received = True
        break
    except:
        print('警告：NTP 服务器 {} ({}/{}) 无响应。'.format(conf['servers'][i],i+1,len(conf['servers'])))

if received:
    date = datetime.fromtimestamp(resp).strftime('%Y-%m-%d')
    time = datetime.fromtimestamp(resp).strftime('%H:%M:%S')
    print(f'转换时间戳到日期 {date} 时间 {time}')
else:
    print('错误：预置列表内的所有 NTP 服务器均无响应。')
    if not conf['abort']:
        date = input('请手动输入当前日期 (格式 YYYY-mm-dd)：')
        time = input('请手动输入当前时间 (格式 HH:MM:SS)：')
    else:
        writeBAT = False

if writeBAT:
    with open('sync.bat','w',encoding='gbk') as bat:
        bat.write('''@ECHO OFF
setlocal

set servers=''')
        for i in conf['servers']:
            bat.write(f'{i} ')
        bat.write(f'''

DATE {date}
TIME {time}

net start w32time
w32tm /config /manualpeerlist:"%servers%" /syncfromflags:manual /reliable:yes /update
w32tm /resync
w32tm /query /status
DEL sync.bat''')

    system('sync.bat')

    print('当前本地时间：{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

if not conf['autoexit']:
    print() # 空行需进行测试
    none = input('请按 Enter 键退出...')
