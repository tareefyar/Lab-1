import matplotlib.pyplot as plt
import cv2

#RGB of HHQ
Q1 = cv2.imread(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HHQ.2_UA.tif")
HHQ_rgb =cv2.cvtColor(Q1, cv2.COLOR_BGR2RGB)
plt.imshow(HHQ_rgb)
plt.axis('off')
plt.title("RGB of HHQ")
plt.show()

#RGB of HVQ
Q2 = cv2.imread(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HVQ.2_UA.tif")
HVQ_rgb =cv2.cvtColor(Q2, cv2.COLOR_BGR2RGB)
plt.imshow(HVQ_rgb)
plt.axis('off')
plt.title("RGB of HVQ")
plt.show()