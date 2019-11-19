import os
import pytesseract
try:
  from PIL import Image
except:
  import Image

IMG_DIR = 'imgs'
ALLOWED_EXTENSIONS = {'jpg', 'png'}

def img2text(img_fn):
  text = pytesseract.image_to_string(Image.open('{}/{}'.format(IMG_DIR, img_fn)))
  print(text)
  return text

def ocr_dir():
  for fn in os.listdir(IMG_DIR):
    ext = fn.split('.')[-1]
    if ext not in ALLOWED_EXTENSIONS: continue
    print(fn)
    text = img2text(img_fn=fn)
     

if __name__ == '__main__':
  ocr_dir()



