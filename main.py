from keyboard_listener import alt_keyboard_listener
from pynput import keyboard

def main():
    listener = alt_keyboard_listener()
    #
    def on_press(key):
        listener.on_press(key)

    def on_release(key):
        listener.on_release(key)

    with keyboard.Listener(on_press=on_press, on_release=on_release) as kb_listener:
        print("Программа запущена. Используйте Alt + стрелки для управления.")
        print("Alt + ↑ - увеличение скорости")
        print("Alt + ↓ - уменьшение скорости") 
        print("Alt + ← - левый клик мыши")
        print("Alt + → - правый клик мыши")
        print("Стрелки без Alt - перемещение мыши")
        kb_listener.join()

if __name__ == '__main__':
    main()