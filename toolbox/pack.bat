@ECHO OFF

:loop
CLS
ECHO ���� 1 ���д����
ECHO ���� 2 ���߰�װ pyinstaller��
ECHO ���� 3 ���߰�װ ntplib��
CHOICE /C 0123 /N /M "���� 0 �˳���"
if errorlevel 4 goto ntplib
if errorlevel 3 goto pyinstaller
if errorlevel 2 goto pack
if errorlevel 1 goto exit
if errorlevel 0 goto exit
goto loop

:pack
CLS
pyinstaller --hidden-import ntplib.NTPClient --version-file file_version_info.txt -F ../synchronizer.py
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
