import os
import pytesseract
try:
  from PIL import Image
except:
  import Image

IMG_DIR = 'imgs/300dpi'
ALLOWED_EXTENSIONS = {'jpg', 'png'}
LANG = 'ita'
TRAINEDDATA_DIR = 'traineddata'

def img2text(img_fn):
  tessdata_dir_config = r'--tessdata-dir "{}/"'.format(TRAINEDDATA_DIR)
  img = Image.open('{}/{}'.format(IMG_DIR, img_fn))
  print('{}. Image dpi = {}'.format(img_fn, img.info['dpi']))
  text = pytesseract.image_to_string(img, lang=LANG, config=tessdata_dir_config)
  print(text)
  return text

def ocr_dir():
  for fn in os.listdir(IMG_DIR):
    ext = fn.split('.')[-1]
    if ext not in ALLOWED_EXTENSIONS: continue
    text = img2text(img_fn=fn)

if __name__ == '__main__':
  ocr_dir()
  #img2text('WP_001871.jpg')



