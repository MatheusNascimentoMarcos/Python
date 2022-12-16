import pyautogui
import pyperclip
import time
import os


pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('Edge')
pyautogui.press('enter')
time.sleep(6)
pyperclip.copy('https://tasks.office.com/dominos.com.br/pt-BR/Home/Planner/#/plantaskboard?groupId=42f50351-f060-4e20-b596-d81c0438260d&planId=B3WHEWd7C0uTueBiZzEo0GUACV8g')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(15)
pyautogui.click(x = 879,y = 148)
time.sleep(5)
pyautogui.click(x = 834,y = 436)
time.sleep(15)
#-------------------------------------------transferencia de pasta-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
src=r"C:\Users\matheus.marcos\Downloads\Saneamento Mapa Domino's.xlsx"
des=r"C:\Users\matheus.marcos\OneDrive - dominosbrasil\Dominos - Matheus\Saneamento\Saneamento Mapa Domino's.xlsx"
os.replace(src,des)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pyautogui.hotkey('ctrl','t')
pyperclip.copy('https://dominosbrasil.sharepoint.com/sites/ProjetoBI791/Documentos%20Compartilhados/Forms/AllItems.aspx?id=%2Fsites%2FProjetoBI791%2FDocumentos%20Compartilhados%2FGeneral%2FReposit%C3%B3rio%20BI%2FPlanner&viewid=ad6f152f%2Dae99%2D447b%2D8d17%2D5e13c8abab08&OR=Teams%2DHL&CT=1654014306419&params=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMjA1MDEwMTAwOSJ9')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(7)
pyautogui.click(x = 271,y = 254)
time.sleep(1)
pyautogui.click(x = 299,y = 284)
time.sleep(4)
pyautogui.click(x = 356,y = 58)
time.sleep(4)
pyperclip.copy('C:/Users/matheus.marcos/OneDrive - dominosbrasil/Dominos - Matheus/Saneamento')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x = 326,y = 152)
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x = 1074,y = 458)
pyautogui.hotkey('alt','f4')
