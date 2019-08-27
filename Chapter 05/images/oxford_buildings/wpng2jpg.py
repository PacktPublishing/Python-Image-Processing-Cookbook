import cv2
import glob

for imfile in glob.glob('*.png'):
	cv2.imwrite(imfile[:-4] + '.jpg', cv2.imread(imfile))
