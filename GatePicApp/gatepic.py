import os
import sys
from PIL import Image

VALID_IMAGES = [".jpg",".png",".bmp"]


def create_directory(path):
	if not os.path.exists(path):
	    os.makedirs(path)

def check_path(path):
	return bool(os.path.exists(path))

def main(path):
	count = 0
	other_files = 0

	if check_path(path):
		directory_path = path + '/GatePics/'
	for filename in os.listdir(path):
			extension=os.path.splitext(filename)[1]
			if extension.lower() not in VALID_IMAGES:
				continue
			else :
				if count == 0:
					create_directory(directory_path)
				count += 1
				image_file_name = path + '/' + filename	
				img = Image.open(image_file_name)
				img = img.resize((480,640), Image.ANTIALIAS)
				img.save(directory_path + '/' +'GatePic.jpg')

if __name__ == '__main__':
	path = sys.argv[1]
	path = os.path.abspath(path)
	main(path)
