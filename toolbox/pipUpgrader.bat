@ECHO OFF

:loop
set /p ask="���� 1 ���� pip������ 2 �� pip Դ����Ϊ�廪��ѧ��Դ�������վ������ 3 �˳���"
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