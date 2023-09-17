from PIL import Image
from pyautogui import screenshot
from pytesseract import image_to_string, pytesseract
from keyboard import add_hotkey, wait

def take_print():
    printscreen = screenshot()
    printscreen.save('print.png')
    print('print tirado com sucesso')
    imagem = Image.open('print.png')
    pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    text = img_to_str(imagem)
    print(text)
    

def img_to_str(img):
    return image_to_string(img)
    

add_hotkey('ctrl+shift+s', take_print)
print('Pressione Ctrl + Shift + S para traduzir a imagem')



wait('esc')
