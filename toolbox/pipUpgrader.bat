@ECHO OFF

:loop
CLS
ECHO ���� 1 ���� pip��
ECHO ���� 2 �� pip Դ����Ϊ�廪��ѧ��Դ�������վ��
CHOICE /C 012 /N /M "���� 0 �˳���"
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