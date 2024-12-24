# !Python3
# !Автокликер для игр в telegram

import subprocess, time, pyautogui, random

program_path = "C:\Program Files\BlueStacks_nxt\HD-Player.exe"
telegram_coordinate = 965, 460
search_coordinate = 950, 220
write_Bums = 'Bums'
write_1win = '1win'
chat_coordinate = 670, 430
app_coordinate = 1060, 1180
accept_button_coordinate = 1280, 960
tap_coordinate = 1400, 700
close_coordinate = 900, 230
close_coordinate_accept = 1500, 770

# открытие эмулятора
subprocess.Popen(program_path)
time.sleep(15)

# открытие telegram
def start_telegram():
    pyautogui.click(telegram_coordinate)
    time.sleep(15)

# поиск и открытие приложения
def open_app(write_name_app):
    pyautogui.click(search_coordinate)
    pyautogui.typewrite(write_name_app)
    time.sleep(2)
    pyautogui.click(chat_coordinate)
    time.sleep(2)
    pyautogui.click(app_coordinate)
    time.sleep(20)

def close_app():
    pyautogui.click(close_coordinate)
    time.sleep(1)
    pyautogui.click(close_coordinate_accept)

# нажать кнопку 
def click_accept():
    pyautogui.moveTo(accept_button_coordinate)

# тапаем тапалку
def tap_game():
    x, y = tap_coordinate
    for i in range (0, random.randint(180, 230)):
        pyautogui.click(x * random.uniform(0.8, 1.1), y * random.uniform(0.8, 1.15))
        time.sleep(0.2 * random.uniform(0.6, 1.1))

start_telegram()


try:
    while True:
        open_app(write_Bums)
        click_accept()
        tap_game()
        close_app()
        time.sleep(3)
        open_app(write_1win)
        click_accept()
        tap_game()
        close_app()
        time.sleep(240 * random.uniform(0.8, 1.1))
except KeyboardInterrupt:
    pass
