# !Python3
# !Автокликер для игр в telegram

import subprocess, time, pyautogui

program_path = "C:\Program Files\BlueStacks_nxt\HD-Player.exe"
telegram_coordinate = 950, 500
search_coordinate = 935, 250
write_Bums = 'Bums'
bums_coordinate = 910, 430

subprocess.Popen(program_path)
time.sleep(10)

# запускаем telegram
pyautogui.click(telegram_coordinate)
time.sleep(15)

# выбираем поиск
pyautogui.click(search_coordinate)

# запускаем Bums
pyautogui.typewrite(write_Bums)
pyautogui.click(bums_coordinate)