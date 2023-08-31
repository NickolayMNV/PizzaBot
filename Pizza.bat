@echo off

call %~dp0"PizzaBot\venv\Scripts\activate"  

cd %~dp0PizzaBot

set TOKEN=6375956995:AAH4pVmqXjtwjja6M9sYb_XuzGp5xClHc3s

python bot_telegram.py 

pause