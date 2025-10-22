import logging as log
import typing as t
from pynput import keyboard as kb
import pyautogui as pg

class alt_keyboard_listener:

    def __init__(self):
        self.alt_key_clicked = False
        self.speed = 10


    def on_press(self, key):
        self.alt_key_clicked = True

        if key in [kb.Key.up, kb.Key.down, kb.Key.left, kb.Key.right]:
            if self.alt_key_clicked:
                if key == kb.Key.left:
                    pg.click(button='left')
                    print("Левый клик мыши (Alt + ←)")
                elif key == kb.Key.right:
                    pg.click(button='right')
                    print("Правый клик мыши (Alt + →)")
                elif key == kb.Key.up:
                    self.speed += 5
                    print(f"Скорость увеличена: {self.speed}")
                elif key == kb.Key.down:
                    self.speed = max(1, self.speed - 5)
                    print(f"Скорость уменьшена: {self.speed}")

            else:
                if key == kb.Key.up:
                    pg.moveRel(0, -self.speed)
                elif key == kb.Key.down:
                    pg.moveRel(0, self.speed)
                elif key == kb.Key.left:
                    pg.moveRel(-self.speed, 0)
                elif key == kb.Key.right:
                    pg.moveRel(self.speed, 0)
    
    def on_release(self, key):
        if key == kb.Key.alt:
            self.alt_key_clicked = False
            print("Alt отпущена - режим перемещения мыши активирован")