import cv2
from pytesseract import image_to_string, pytesseract
from keyboard import add_hotkey, wait

def page_to_panels():
    img = cv2.imread('page/page.jpg')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # dá um realce nas bordas para utilizar o método de Canny
    edges = cv2.Canny(img_gray, threshold1=100, threshold2=200)
    contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]


def img_to_str():
    img = cv2.imread('page/page.jpg')
    text = image_to_string(img)
    print('\nTexto:\n\n' + text)


# define onde está o tesseract  
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# cria atalho e diz o que ele deve fazer
add_hotkey('ctrl+shift+a', page_to_panels)
print('Pressione Ctrl + Shift + A para traduzir a imagem')

wait('esc')
