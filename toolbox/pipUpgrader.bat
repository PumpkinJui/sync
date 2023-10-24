@ECHO OFF

:loop
CLS
ECHO 输入 1 更新 pip；
ECHO 输入 2 将 pip 源更改为清华大学开源软件镜像站；
CHOICE /C 012 /N /M "输入 0 退出："
if errorlevel 3 goto mirror
if errorlevel 2 goto upgrade
if errorlevel 1 goto exit
if errorlevel 0 goto exit
goto loop

:upgrade
CLS
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
pause
goto loop

:mirror
CLS
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pause
goto loop

:exit
exit