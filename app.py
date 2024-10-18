# Importar biblioteca de automação 
# instalação do cx Freeze: pip install cx_Freeze
# comando para gerar executável: cxfreeze app.py --target-fir nome-pasta

import pyautogui as auto 

auto.PAUSE = 0.7 

auto.press("win")
auto.write("edge")
auto.press("enter")
auto.hotkey("alt", "sapce")
auto.press("x")
auto.write("python.org")
auto.press("enter")
auto.hotkey("ctrl","t")
auto.write("google.com.br")
auto.press("enter")
auto.write("https://pyautogui.readthedocs.io/en/latest/install.html")
auto.press("enter")

for i in range(23):
    auto.press("tab")

auto.press("enter")
