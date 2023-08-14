import rasterio
import matplotlib.pyplot as plt

#Meta data about tiff image

Q1 = rasterio.open(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HHQ.2_UA.tif")
Q2 = rasterio.open(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HVQ.2_UA.tif")

#META DATA OF HHQ
width = Q1.width
height = Q1.height
print("Size of HHQ (Width x Height) is", width, 'x', height)


n_bands = Q1.count
print("Number of Bands of HHQ are: ", n_bands)

Q1.width
Q1.height
Q1.count

plt.imshow(Q1.read(1))
plt.show()
Q1.close()

#META DATA OF HVQ
width = Q2.width
height = Q2.height

print("Size of HVQ (Width x Height) is", width, 'x', height)
n_bands = Q2.count
print("Number of Bands of HVQ are: ", n_bands)

Q2.width
Q2.height
Q2.count

plt.imshow(Q2.read(1))
plt.show()
Q2.close()