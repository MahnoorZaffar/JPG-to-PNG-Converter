from PIL import Image, ImageFilter
import sys
import os

img_path = sys.argv[1]
new_path = sys.argv[2]

if not os.path.exists(new_path):
    os.makedirs(new_path)

for file in os.listdir(img_path):
    img = Image.open(f'{img_path}{file}')
  
    # new_file = file.replace(".jpg", ".png") 
  
    new_file = os.path.splitext(file)[0]    
    img.save(f"{new_path}/{new_file}.png", "png")

