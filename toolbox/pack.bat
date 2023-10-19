@ECHO OFF

:loop
set /p ask="输入 0 进行打包，输入 1 在线安装 pyinstaller，输入 2 在线安装 ntplib，输入 3 退出："
if /i %ask%==0 goto pack
if /i %ask%==1 goto pyinstaller
if /i %ask%==2 goto ntplib
if /i %ask%==3 goto exit
goto loop

:pack
pyinstaller --hidden-import ntplib.NTPClient --version-file file_version_info.txt -F synchronizer.py
pause
goto loop

:pyinstaller
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
pause
goto loop

:ntplib
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ntplib
pause
goto loop

:pack
pip install ntplib-0.4.0-py2.py3-none-any.whl
pause
goto loop

:exit
exit
