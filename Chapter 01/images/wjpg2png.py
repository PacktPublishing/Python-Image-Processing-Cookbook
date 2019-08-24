import cv2
import glob

for imfile in glob.glob('*.jpg'):
	cv2.imwrite(imfile[:-4] + '.png', cv2.imread(imfile))
