from pyautogui import screenshot
from keyboard import add_hotkey, wait

def take_print():
    printscreen = screenshot()
    printscreen.save('print.png')
    print('print tirado com sucesso')

add_hotkey('ctrl+shift+s', take_print)
print('Pressione Ctrl + Shift + S para traduzir a imagem')

wait('esc')
