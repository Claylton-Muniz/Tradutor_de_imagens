import cv2
from pytesseract import image_to_string, pytesseract
from keyboard import add_hotkey, wait

def img_to_str():
    imagem = cv2.imread('page/page.jpg')
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    bordas = cv2.Canny(imagem_cinza, threshold1=100, threshold2=200)
    # cv2.imwrite('img_tests/test.jpg', bordas)
    cv2.imshow('bordas', cv2.resize(bordas, (0, 0), fx=0.3, fy=0.2))
    cv2.waitKey(0)
    text = image_to_string(imagem)
    print('\nTexto:\n\n' + text)

  
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

add_hotkey('ctrl+shift+a', img_to_str)
print('Pressione Ctrl + Shift + A para traduzir a imagem')

wait('esc')
