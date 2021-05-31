from google_images_download import google_images_download
import argparse
import os
import shutil
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--keywords',
                    help="type as 'cat,dog'", type=str, required=True)
parser.add_argument(
    '-n', '--nums', help='input total images count', type=int, required=True)
parser.add_argument(
    '-r', '--val_ratio', help='train val split ratio', type=float, default=0.2
)
args = parser.parse_args()

response = google_images_download.googleimagesdownload()
base_folder = '-'.join(args.keywords.split(','))
os.makedirs(base_folder, exist_ok=True)
os.chdir(base_folder)
arguments = {"keywords": args.keywords,
             "limit": args.nums,
             "format": "jpg",
             "output_directory": "train"}
response.download(arguments)

classes = args.keywords.split(",")

# Make val folder
for class_name in classes:
    os.makedirs(os.path.join('./val', class_name), exist_ok=True)

for class_name in classes:
    images = os.listdir(os.path.join('./train', class_name))
    for image in images:
        if image.split('.')[-1] == 'webp':
            origin_image = os.path.join('./train', class_name, image)
            try:
                img = Image.open(origin_image).convert('RGB')
                img.save(origin_image[:-5])  # remove .webp in name
            except:
                pass
            os.remove(origin_image)

for class_name in classes:
    images = os.listdir(os.path.join('./train', class_name))
    total_cnt = len(images)
    val_cnt = int(total_cnt * args.val_ratio)
    for i, image in enumerate(sorted(images)):  # sorted effect as shuffle
        new_image_name = str(i+1).zfill(5) + '.jpg'
        if i < val_cnt:
            shutil.move(os.path.join('./train', class_name, image),
                        os.path.join('./val', class_name, new_image_name))
        else:
            shutil.move(os.path.join('./train', class_name, image),
                        os.path.join('./train', class_name, new_image_name))

print("\n\n Complete!!")
