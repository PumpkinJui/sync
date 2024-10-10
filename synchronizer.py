# https://blog.csdn.net/xy3233/article/details/122405558

from datetime import datetime
from json import load
from ntplib import NTPClient
from os import system

try:
    with open('sync.json','r') as confR:
        conf = load(confR)
    print('配置文件读取成功！')
except: # 当文件中只有一部分配置时，还是会报错
    print('未读取到合法的配置文件，将使用默认配置...')
    conf = {'abort': False, 'pause': True}

print()

print('当前本地时间：{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

ntpc = NTPClient()
received = False
writeBAT = True

servers = ['time.windows.com','cn.ntp.org.cn','cn.pool.ntp.org','ntp.ntsc.ac.cn']
for i in range(4):
    try:
        resp = ntpc.request(servers[i]).tx_time
        print(f'收到 NTP 服务器 {servers[i]} 回复，当前时间戳为',resp)
        received = True
        break
    except:
        print(f'NTP 服务器 {servers[i]} ({i+1}/4) 无响应。')

if received:
    date = datetime.fromtimestamp(resp).strftime('%Y-%m-%d')
    time = datetime.fromtimestamp(resp).strftime('%H:%M:%S')
    print(f'转换时间戳到日期 {date} 时间 {time}')
else:
    print('预置列表内的所有 NTP 服务器均无响应。')
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
        for i in servers:
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

if conf['pause']:
    print()
    none = input('请按 Enter 键退出...')
