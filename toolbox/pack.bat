@ECHO OFF

:loop
CLS
ECHO 输入 1 进行普通版的打包；
ECHO 输入 2 进行简洁版的打包；
ECHO 输入 3 在线安装 pyinstaller；
ECHO 输入 4 在线安装 ntplib；
CHOICE /C 01234 /N /M "输入 0 退出："
if errorlevel 5 goto ntplib
if errorlevel 4 goto pyinstaller
if errorlevel 3 goto pack_lite
if errorlevel 2 goto pack
if errorlevel 1 goto exit
if errorlevel 0 goto exit
goto loop

:pack
CLS
pyinstaller --hidden-import ntplib.NTPClient --version-file file_version_info.txt -F ../synchronizer.py
pause
goto loop

:pack_lite
CLS
pyinstaller --hidden-import ntplib.NTPClient --version-file file_version_info_lite.txt -F ../synchronizer_lite.py
pause
goto loop

:pyinstaller
CLS
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
pause
goto loop

:ntplib
CLS
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ntplib
pause
goto loop

:exit
exit
