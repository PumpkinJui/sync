# https://blog.csdn.net/xy3233/article/details/122405558

from ntplib import NTPClient
from datetime import datetime
from os import system

print('当前本地时间：{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

ntpc = NTPClient()
received = False

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
    date = input('请手动输入当前日期 (格式 YYYY-mm-dd)：')
    time = input('请手动输入当前时间 (格式 HH:MM:SS)：')

bat = open('sync.bat','w',encoding='gbk')
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
DEL sync.bat''')
bat.close()

system('sync.bat')
