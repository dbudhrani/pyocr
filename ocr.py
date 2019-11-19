import os
import sys
import cv2
import pytesseract
from matplotlib import pyplot as plt

try:
  from PIL import Image
except:
  import Image

IMG_DIR = 'imgs'
XDPI_IMG_DIR = 'imgs/300dpi'
RESIZED_IMG_DIR = '{}/resized'.format(IMG_DIR)
ALLOWED_EXTENSIONS = {'jpg', 'png'}
LANG = 'ita'
TRAINEDDATA_DIR = 'traineddata'
THRESHOLD = int(sys.argv[1])

def resize_image(path, img_fn):
  basewidth = 7200
  img = Image.open('{}/{}'.format(path, img_fn))
  wpercent = (basewidth/float(img.size[0]))
  hsize = int((float(img.size[1])*float(wpercent)))
  img = img.resize((basewidth,hsize), Image.ANTIALIAS)
  plot_img(img)
  img.save('{}/{}'.format(RESIZED_IMG_DIR, img_fn))

def threshold(path, img_fn):
  fp = '{}/{}'.format(path, img_fn)
  img = cv2.imread(fp, cv2.CV_8UC1)
  img = cv2.medianBlur(img,5)
  _, img_binarized = cv2.threshold(img, THRESHOLD, 255, cv2.THRESH_BINARY)
  #img_binarized = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
  return Image.fromarray(img_binarized)

def plot_img(img):
  plt.imshow(img,'gray')
  plt.title('img')
  plt.xticks([]),plt.yticks([])
  plt.show()  

def img2text(path=None, img_fn=None, img=None):
  if path and img_fn:
    img = Image.open('{}/{}'.format(path, img_fn))
    #print('{}. Image dpi = {}'.format(img_fn, img.info['dpi']))
  assert img
  #plot_img(img)
  tessdata_dir_config = r'--tessdata-dir "{}/"'.format(TRAINEDDATA_DIR)
  text = pytesseract.image_to_string(img, lang=LANG, config=tessdata_dir_config)
  print(text)
  return text

def ocr_dir():
  for fn in os.listdir(IMG_DIR):
    ext = fn.split('.')[-1]
    if ext not in ALLOWED_EXTENSIONS: continue
    #resize_image(path=XDPI_IMG_DIR, img_fn=fn)
    #img = threshold(path=XDPI_IMG_DIR, img_fn=fn)
    #text = img2text(path=RESIZED_IMG_DIR, img=img)
    text = img2text(path=XDPI_IMG_DIR, img_fn=fn)

if __name__ == '__main__':
  ocr_dir()
  #img2text(path=RESIZED_IMG_DIR, img_fn='WP_001880.jpg')



