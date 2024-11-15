@echo off
IF EXIST "C:\Program Files\Git\bin\bash.exe" (
    "C:\Program Files\Git\bin\bash.exe" --login -i -c "cd .. && source ./venv/Scripts/activate && python main.py"
) ELSE (
    echo Git Bash not found in the expected location
    echo Please install Git or correct the path
)
pause
