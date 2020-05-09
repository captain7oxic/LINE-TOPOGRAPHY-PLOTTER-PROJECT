import tifffile as tiff
import numpy as np
import cv2


directory = "C:\\Users\\Vatsal\\Desktop\\codes\\Line-topography-plotter-project\\"
name = 'srtm_53_08'

map = tiff.imread(directory + name + '.tif')
resize_factor = 10
new_shape = (int(map.shape[1]/resize_factor),
             int(map.shape[0]/resize_factor))  # reversed for cv2

map = cv2.resize(map, new_shape, interpolation=cv2.INTER_NEAREST)

tiff.imwrite(directory + name + '__' + str(map.shape) +
             '.tiff', map, planarconfig='CONTIG')
