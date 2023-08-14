from PIL import Image
import numpy as np


#open image
Q1 = Image.open(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HHQ.2_UA.tif")
Q2 = Image.open(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HVQ.2_UA.tif")

#HHQ
#convert image to numpy array
HHQ_array = np.array(Q1)

#Calculate the image statistics
mean = np.mean(HHQ_array)
std_dev = np.std(HHQ_array)
min = np.min(HHQ_array)
max = np.max(HHQ_array)

#print
print("Statistics of HHQ")
print("Mean of HHQ:", mean)
print("Standard Deviation of HHq:", std_dev)
print("Min of HHQ:", min)
print("Max of HHQ:", max)

width, height = Q1.size
print("Widthof HHq:", width)
print("Height: of HHQ", height)

#HVQ
#convert image to numpy array
HVQ_array = np.array(Q1)

#Calculate the image statistics
mean = np.mean(HVQ_array)
std_dev = np.std(HVQ_array)
min = np.min(HVQ_array)
max = np.max(HVQ_array)

#print
print("\n Statistics of HHQ")
print("Mean of HVQ:", mean)
print("Standard Deviation of HVQ:", std_dev)
print("Min of HVQ:", min)
print("Max of HVQ:", max)

width, height = Q1.size
print("Widthof HVQ:", width)
print("Height: of HVQ", height)