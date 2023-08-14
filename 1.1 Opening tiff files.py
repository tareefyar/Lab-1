from rasterio.plot import show
from PIL import Image


# reading tiff file
Q1 = Image.open(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HHQ.2_UA.tif")
Q2 = Image.open(r"E:\6th Semester\Image Processing\Lab Works\IP\Quetta.2_UA\HVQ.2_UA.tif")
show(Q1)
pixels = Q1.load()
show(Q2)
pixels = Q2.load()