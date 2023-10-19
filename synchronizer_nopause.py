# https://blog.csdn.net/xy3233/article/details/122405558

from ntplib import NTPClient
from datetime import datetime
from os import system

print('当前本地时间：{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

ntpc = NTPClient()
received = True
try:
    resp = ntpc.request('time.windows.com').tx_time
except:
    try:
        resp = ntpc.request('cn.ntp.org.cn').tx_time
    except:
        try:
            resp = ntpc.request('cn.pool.ntp.org').tx_time
        except:
            try:
                resp = ntpc.request('ntp.ntsc.ac.cn').tx_time
            except:
                received = False

if received:
    print('收到 NTP 服务器回复，当前时间戳为',resp)
    date = datetime.fromtimestamp(resp).strftime('%Y-%m-%d')
    print('转换时间戳到日期',date)
else:
    print('NTP 服务器无响应。')
    date = input('请手动输入当前日期 (格式 YYYY-mm-dd)：')

bat = open('sync.bat','w',encoding='gbk')
bat.write('@ECHO OFF\n\n')
bat.write('DATE {}\n'.format(date))
bat.write('TIME 12:00:00\n\n')
bat.write('net start w32time\n')
bat.write('w32tm /resync\n\n')
bat.write('DEL sync.bat')
bat.close()

system('sync.bat')

print('当前本地时间：{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
