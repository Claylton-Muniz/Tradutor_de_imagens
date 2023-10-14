from googletrans import Translator

# Inicialize o tradutor
translator = Translator()

# Texto a ser traduzido
text = "Hello, world!"

# Traduza o texto para o idioma desejado, por exemplo, 'pt' para Português
translated_text = translator.translate(text, dest='pt')

# Imprima a tradução
print(translated_text.text)