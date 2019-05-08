import os
from PIL import Image

path = 'png'
maxsize = (200, 500)

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
	for file in f:
		if not '.nfo' in file:
			im = Image.open(os.path.join(r, file))
			im.thumbnail(maxsize, Image.ANTIALIAS)
			im.save(os.path.join(r, file.split('.')[0] + '.png'))
		if '.jpg' in file:
			os.remove(os.path.join(r, file))
		f = open(os.path.join(r, file.split('.')[0] + '.nfo'),"w+")
		f.write("Bitmap=" + file.split('.')[0] + '.png' )
print "Done"