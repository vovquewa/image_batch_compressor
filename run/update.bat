@echo off
IF EXIST "C:\Program Files\Git\bin\bash.exe" (
    "C:\Program Files\Git\bin\bash.exe" --login -i -c "cd .. && git pull"
) ELSE (
    echo Git Bash not found in the expected location
    echo Please install Git or correct the path
)
pause
