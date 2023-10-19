@ECHO OFF

:loop
set /p ask="输入 1 在线安装 ntplib，输入 2 离线安装 ntplib，输入 3 退出："
if /i %ask%==1 goto online
if /i %ask%==2 goto offline
if /i %ask%==3 goto exit
goto loop

:online
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ntplib
pause
goto loop

:offline
pip install ntplib-0.4.0-py2.py3-none-any.whl
pause
goto loop

:exit
exit