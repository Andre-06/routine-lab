import random
import pyautogui as pg
from time import sleep
from datetime import datetime
from getpass import getpass

psw = getpass("Senha: ")
pg.PAUSE = 1
big_wait = 10
middle_wait = 6

pg.press("win")
pg.write("firefox")
pg.press("enter")
sleep(20)
pg.hotkey("ctrlleft", "l")
pg.write("https://github.com/login")
pg.press("enter")
sleep(middle_wait)
pg.write("Andre-06")
pg.press("tab")
pg.write(psw)   
pg.press("enter")
sleep(10)
pg.hotkey("ctrlleft", "l")
pg.write("https://github.com/settings/tokens/new")
pg.press("enter")
sleep(middle_wait)
pg.write("token-lab-" + str(random.randint(1, 9999)))
pg.press("tab")
pg.press("enter")
pg.press("down")
pg.press("down")
pg.press("down")
pg.press("enter")
pg.press("tab")

now = datetime.now()

pg.write(str(int(now.strftime("%d")) + 1))
pg.write(datetime.now().strftime("%m"))
pg.write(datetime.now().strftime("%Y"))

pg.press("tab")
pg.press("tab")
pg.press("space")
pg.press("enter")

sleep(middle_wait)
pg.hotkey("ctrlleft", "t")
sleep(middle_wait)
pg.write("eadcampus.spo.ifsp.edu.br/login/index.php")
pg.press("enter")
sleep(middle_wait)
pg.press("tab")
pg.press("tab")
pg.press("tab")
pg.press("enter")
sleep(big_wait)
pg.write("SP3089789")
pg.press("enter")
pg.write(psw[:-1] + "7")
pg.press("enter")

sleep(big_wait + 2)
pg.hotkey("ctrlleft", "l")
pg.write("https://eadcampus.spo.ifsp.edu.br/course/view.php")
pg.hotkey("altright", "w")
pg.write("id=9344")
pg.press("enter")
