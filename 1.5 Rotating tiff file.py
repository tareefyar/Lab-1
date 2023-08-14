import cv2
import matplotlib.pyplot as plt

try:
    # Read image from disk.
    Q1 = cv2.imread(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HHQ.2_UA.tif")
 
     # Shape of image in terms of pixels.
    (rows, cols) = Q1.shape[:2]
 
    # getRotationMatrix2D creates a matrix needed for transformation.
    # We want matrix for rotation w.r.t center to 45 degree without scaling.
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    R_HHQ = cv2.warpAffine(Q1, M, (cols, rows))
 
    # Write image back to disk.
    cv2.imwrite('result.tiff', R_HHQ)
    plt.imshow(R_HHQ)
    plt.title("Rotated HHQ")
    plt.show()
 
except IOError:
    print('Error while reading files !!!')

try:
    # Read image from disk.
    Q2 = cv2.imread(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HVQ.2_UA.tif")
 
     # Shape of image in terms of pixels.
    (rows, cols) = Q2.shape[:2]
 
    # getRotationMatrix2D creates a matrix needed for transformation.
    # We want matrix for rotation w.r.t center to 45 degree without scaling.
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    R_HVQ = cv2.warpAffine(Q2, M, (cols, rows))
 
    # Write image back to disk.
    cv2.imwrite('result.tiff', R_HVQ)
    plt.imshow(R_HVQ)
    plt.title("Rotated HVQ")
    plt.show()
 
except IOError:
    print('Error while reading files !!!')
