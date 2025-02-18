from get_construction import get_construction
import keyboard
import pyperclip
import pyautogui
import time
from pystray import Icon, MenuItem, Menu
from PIL import Image
import threading
from pynput.keyboard import Controller, Listener


def insert_text_to_clipboard(text):
    pyperclip.copy(text)


def paste_text():
    pyautogui.hotkey('ctrl', 'v')


def modify_copied_text():
    time.sleep(0.1)
    text = pyperclip.paste()

    if text: return get_construction(text.strip())



def listen_for_hotkeys():
    print("Скрипт запущен")

    while True:
        if keyboard.is_pressed('ctrl+c'):

            modified_text = modify_copied_text()
            print(modified_text)
            if modified_text:
                insert_text_to_clipboard(modified_text)
                time.sleep(0.1)
                paste_text()

        time.sleep(0.1)


listen_for_hotkeys()





# -----------------

# def on_quit(icon, item):
#     """Закрыть приложение."""
#     icon.stop()


# def run_tray_app():
#     """Запуск приложения в трее."""
#     # Создание иконки
#     icon = Icon("app_name")
#     icon.icon = Image.open('icon.png')

#     # Создание меню с пунктом для выхода
#     icon.menu = Menu(MenuItem("Quit", on_quit))

#     # Запуск горячих клавиш в отдельном потоке
#     threading.Thread(target=listen_for_hotkeys, daemon=True).start()

#     # Запуск иконки
#     icon.run()



# run_tray_app()
