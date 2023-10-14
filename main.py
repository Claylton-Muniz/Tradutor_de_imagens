import cv2
from googletrans import Translator
from pytesseract import image_to_string, pytesseract
from keyboard import add_hotkey, wait

translator = Translator()

def img_to_str(end):
    text = ''
    for i in range(0, end):
        img = cv2.imread(f'page/page-{i}.jpg')
        text += image_to_string(img)
    print('\nTexto:\n\n' + text)
    translated_text = translator.translate(text, dest='pt', src='en')
    print('\nTradução:\n\n', translated_text)


# define onde está o tesseract  
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

num_panels = int(input('Quantos quadros voce printou? '))

# cria atalho e diz o que ele deve fazer
add_hotkey('enter', img_to_str(num_panels-1))
print('Pressione "Enter" para traduzir a imagem')

wait('esc')
