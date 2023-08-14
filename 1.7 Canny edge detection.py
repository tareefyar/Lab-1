import matplotlib.pyplot as plt

import cv2
#canny edge detection of HHQ
try:
    Q1 = cv2.imread(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HHQ.2_UA.tif")
    edges_HHQ = cv2.Canny(Q1, 15, 10)
    cv2.imwrite("Canny Edge of HHQ.tiff", edges_HHQ)
    plt.imshow(edges_HHQ)
    plt.title("Canny Edge of HHQ")
    plt.show()
except IOError:
    print("Error")

#canny edge detection of HVQ
try:
    Q2 = cv2.imread(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HVQ.2_UA.tif")
    edges_HVQ = cv2.Canny(Q2, 15, 10)
    cv2.imwrite("Canny Edge of HVQ.tiff", edges_HVQ)
    plt.imshow(edges_HVQ)
    plt.title("Canny Edge of HVQ")
    plt.show()
except IOError:
    print("Error")