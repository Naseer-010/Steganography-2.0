from lsb import LSBSteg
import cv2

steg = LSBSteg(cv2.imread("nature.png"))
new_im = steg.encode_image(cv2.imread("leaf.jpg"))
cv2.imwrite("new_image.png", new_im)