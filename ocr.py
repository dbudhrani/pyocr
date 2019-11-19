import os
import pytesseract
try:
  from PIL import Image
except:
  import Image

IMG_DIR = 'imgs'
ALLOWED_EXTENSIONS = {'jpg', 'png'}
LANG = 'ita'
TRAINEDDATA_DIR = 'traineddata'

def img2text(img_fn):
  tessdata_dir_config = r'--tessdata-dir "{}/"'.format(TRAINEDDATA_DIR)
  text = pytesseract.image_to_string(Image.open('{}/{}'.format(IMG_DIR, img_fn)), lang=LANG, config=tessdata_dir_config)
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
  #img2text('WP_001871.jpg')



