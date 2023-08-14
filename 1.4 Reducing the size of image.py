import matplotlib.pyplot as plt
import cv2

#Reducing size of the image
try:
    #read image from disk
    Q1 = cv2.imread(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HHQ.2_UA.tif")
    #get no of pixel horizontally and vertically
    (height, width) = Q1.shape[:2]

     # Specify the size of image along with interpolation methods.
    # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC is used for zooming.
    rsize_HHQ = cv2.resize(Q1, (int(width/2), int(height/2)), interpolation = cv2.INTER_CUBIC)

    #write the image back to disk
    cv2.imwrite("HHQ resized.tiff", rsize_HHQ)
    plt.imshow(rsize_HHQ)
    plt.title("HHQ Resized")
    plt.show()
except IOError:
    print("Error while reading tiff file!!!")

#Resizing HHV
try:
    #read image from disk
    Q2 = cv2.imread(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HVQ.2_UA.tif")

    #get no of pixel horizontally and vertically
    (height, width) = Q2.shape[:2]

     # Specify the size of image along with interpolation methods.
    # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC is used for zooming.
    rsize_HVQ = cv2.resize(Q2, (int(width/2), int(height/2)), interpolation = cv2.INTER_CUBIC)

    #write the image back to disk
    cv2.imwrite("HVQ resized.tiff", rsize_HVQ)
    plt.imshow(rsize_HVQ)
    plt.title("HVQ Resized")
    plt.show()
except IOError:
    print("Error while reading tiff file!!!")