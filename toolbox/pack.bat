@ECHO OFF

:loop
set /p ask="���� 1 ������ͨ��Ĵ�������� 2 ��������ͣ��Ĵ�������� 3 ���߰�װ pyinstaller������ 4 ���߰�װ ntplib������ 0 �˳���"
if /i %ask%==1 goto pack
if /i %ask%==2 goto pack_nopause
if /i %ask%==3 goto pyinstaller
if /i %ask%==4 goto ntplib
if /i %ask%==0 goto exit
goto loop

:pack
pyinstaller --hidden-import ntplib.NTPClient --version-file file_version_info.txt -F ../synchronizer.py
pause
goto loop

:pack_nopause
pyinstaller --hidden-import ntplib.NTPClient --version-file file_version_info_nopause.txt -F ../synchronizer_nopause.py
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

:exit
exit
