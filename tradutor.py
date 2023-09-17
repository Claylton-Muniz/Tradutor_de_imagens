from PIL import Image
from pytesseract import image_to_string, pytesseract
from keyboard import add_hotkey, wait

def img_to_str():
    imagem = Image.open('page.jpg')
    text = image_to_string(imagem)
    print('\nTexto:\n\n' + text)

  
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

add_hotkey('ctrl+shift+a', img_to_str)
print('Pressione Ctrl + Shift + A para traduzir a imagem')

wait('esc')
