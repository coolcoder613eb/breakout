@echo off
cd
rem --enable-plugin=numpy
CHOICE /C mo /M "Press M to compile main.pyw or Press O to compile another file."

IF %ERRORLEVEL% == 1 py -m nuitka main.pyw --standalone --onefile --windows-icon-from-ico=icon.ico --enable-plugin=tk-inter 

IF %ERRORLEVEL% == 2 set /P file="which file would you like to compile? "
py -m nuitka %file% --standalone --onefile --windows-icon-from-ico=icon.ico --enable-plugin=tk-inter

pause