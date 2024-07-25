import matplotlib.pyplot as plt
import numpy as np
import os
from skimage import io, img_as_float

# this implements skimage, array loading approach
# need to convert to independent variables for images so that we can implement editing
# this is a stopgap for testing

# set window dimensions to 1080p (optional)
dpi = 100
width_inches = 1920 / dpi
height_inches = 1080 / dpi

# get where image components are stored
components_dir = 'marcel/components'
png_files = [f for f in os.listdir(components_dir) if f.endswith('.png')]

# here you can manually choose what files to load
# array order dictates layer order
manual_order = [
    'base_sky.png',
    'sun_redgiant.png',
    'clouds_sun.png',
    'fuji_base.png',
    'base_ground.png',
    'clouds_fuji.png',
    'clouds_close.png',
    'car_base.png',
    'subject_shadows.png',
    'time_traveller.png'
]

ordered_files = [file for file in manual_order if file in png_files]

# load images in array
images = []
for file in ordered_files:
    image_path = os.path.join(components_dir, file)
    image = img_as_float(io.imread(image_path))
    images.append(image)

plt.figure(1, figsize=(width_inches, height_inches), dpi=dpi)
plt.axis('off')

for image in images:
    plt.imshow(image)

plt.show()