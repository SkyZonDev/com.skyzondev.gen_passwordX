@echo off
color 0A
SETLOCAL ENABLEDELAYEDEXPANSION
 
 
del "%~dpn0_2.bat" 2> nul
for /f "delims=" %%a in (%~dp0Figlet.txt) do (
	set "var=%%~a"
	set var=!var:^^=^^^^!
	set var=!var:^&=^^^&!
	set var=!var:^<=^^^<!
	set var=!var:^>=^^^>!
	set var=!var:^|=^^^|!
	set var=!var:^(=^^^(!
	set var=!var:^)=^^^)!
	set var=!var:%%=%%%%!
 
	echo echo !var!
)>>"%~dpn0_2.bat"
 
call %~dpn0_2.bat
echo.
py main.py

pause