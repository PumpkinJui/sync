# https://blog.csdn.net/xy3233/article/details/122405558

from ntplib import NTPClient
from datetime import datetime
from re import match

ntpc = NTPClient()
try:
    resp = ntpc.request('cn.ntp.org.cn')
except:
    try:
        resp = ntpc.request('time.windows.com')
    except:
        resp = ntpc.request('ntp.ntsc.ac.cn')
tm = str(datetime.fromtimestamp(resp.tx_time)) # xxxx-xx-xx xx:xx:xx.xxxxxx

date = match(r'.*\s',tm).group()

print(date)
