@ECHO OFF

:loop
set /p ask="输入 1 更新 pip，输入 2 将 pip 源更改为清华大学开源软件镜像站，输入 3 退出："
if /i %ask%==1 goto upgrade
if /i %ask%==2 goto mirror
if /i %ask%==3 goto exit
goto loop

:upgrade
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
pause
goto loop

:mirror
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pause
goto loop

:exit
exit