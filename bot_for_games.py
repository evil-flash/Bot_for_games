# !Python3
# !Автокликер для игр в telegram

import subprocess, time, pyautogui, random
import send_message_TG

program_path = "C:\Program Files\BlueStacks_nxt\HD-Player.exe"
telegram_coordinate = 965, 460
search_coordinate = 950, 220
write_Bums = 'Bums'
write_1win = '1win'
chat_coordinate = 670, 430
app_coordinate = 1060, 1180
accept_button_coordinate_1win = 1280, 960
accept_button_coordinate_Bums = 1630, 830
tap_coordinate = 1300, 700
close_coordinate = 900, 230
close_coordinate_accept = 1500, 770
messages = ['Старт цикла', 'Bums оттапан', '1win оттапан', 'Цикл завершён. Ожидание']

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
# закрываем app
def close_app():
    pyautogui.click(close_coordinate)
    time.sleep(1)
    pyautogui.click(close_coordinate_accept)

# нажать кнопку 
def click_accept(accept_button_coordinate):
    pyautogui.moveTo(accept_button_coordinate)
    time.sleep(1)

# тапаем тапалку
def tap_game():
    x, y = tap_coordinate
    for i in range (0, random.randint(400, 530)):
        pyautogui.click(x * random.uniform(0.9, 1.1), y * random.uniform(0.9, 1.1))
        time.sleep(0.1 * random.uniform(0.6, 1.1))

def main():
    start_telegram()
    try:
        while True:
            send_message_TG.send(messages[0])
            open_app(write_Bums)
            click_accept(accept_button_coordinate_Bums)
            tap_game()
            close_app()
            send_message_TG.send(messages[1])
            time.sleep(3)
            open_app(write_1win)
            click_accept(accept_button_coordinate_1win)
            tap_game()
            close_app()
            send_message_TG.send(messages[2])
            send_message_TG.send(messages[3])
            time.sleep(240 * random.uniform(0.8, 1.1))
    except KeyboardInterrupt:
        pass

main()