import pyautogui
import keyboard
import time

def select_text_until_symbol(symbol):
    # Печатаем символы до символа, чтобы выделить текст до первого символа
    # Сначала можно попробовать выделить с использованием стрелок и клавиш Shift
    while symbol != ";":
        pyautogui.hotkey('shift', 'left')  # Зажимаем Shift и идем влево по символам


def listen_for_hotkeys():
    print("Скрипт запущен. Нажмите 'Alt + /' для начала действия.")

    while True:
        if keyboard.is_pressed('ctrl+/'):  # Ждем нажатие Alt + /
            time.sleep(0.1)  # Немного задерживаем, чтобы избежать повторных срабатываний
            select_text_until_symbol(';')  # Выделяем текст до символа ";"
            time.sleep(1)  # Задержка для предотвращения многократного срабатывания

listen_for_hotkeys()


#  вапвапвапук678э|еуке   oiopiopiopipo