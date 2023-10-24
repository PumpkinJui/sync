@ECHO OFF

:loop
CLS
ECHO 输入 1 在线安装 ntplib；
ECHO 输入 2 离线安装 ntplib；
CHOICE /C 012 /N /M "输入 0 退出："
if errorlevel 3 goto offline
if errorlevel 2 goto online
if errorlevel 1 goto exit
if errorlevel 0 goto exit
goto loop

:online
CLS
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ntplib
pause
goto loop

:offline
CLS
pip install ntplib-0.4.0-py2.py3-none-any.whl
pause
goto loop

:exit
exit