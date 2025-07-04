from astropy import units as u
from astropy.coordinates import SkyCoord
from photutils.aperture import CircularAperture
from photutils.aperture import CircularAnnulus, ApertureStats, aperture_photometry

from astropy.time import Time

from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, PowerNorm

import numpy as np
import math

import os


rootdirectory = "insert_root_directory_here"

magnitudes = []
times = []
count = 1


mainfile = fits.open(f"insert_directory_here")
mainfile2 = fits.open(f"insert_directory_here")

fig, ax = plt.subplot()
fig2, ax2 = plt.subplot()

image_pixels = mainfile[0].data
image_pixels_2 = mainfile2[0].data
ax.imshow(image_pixels, origin = "lower", norm = LogNorm())
ax.colorbar()

# get the mjd from the fits file header

header = mainfile[0].header
time_utc = header["DATE-OBS"]
t = Time(time_utc, format = "isot", scale = "utc")
times.append(t.mjd)

pos1 = (852, 680)
pos2 = (619, 568)
positions = np.transpose((pos1, pos2))
apertures = CircularAperture(positions, r = 10.0)
ax.imshow(image_pixels, norm = LogNorm(), interpolation = "nearest")

annulus_aperture = CircularAnnulus(positions, r_in = 15, r_out = 20)

apertures.plot(color = "red", lw = 0.5)
annulus_aperture.plot(color = "green", lw = 0.5)

aperstats = ApertureStats(image_pixels, annulus_aperture)

ax2.imshow(image_pixels_2, origin = "lower", norm = LogNorm())
ax2.colorbar()

star_data = aperture_photometry(image_pixels, apertures)
star_data_2 = aperture_photometry(image_pixels_2, apertures)
for col in star_data.colnames:
    star_data[col].info.format = "%.8g"
    star_data_2[col].info.format = "%.8g"

magnitude_of_hd239746 = 10.04
zero_point = magnitude_of_hd239746 + 2.5 * math.log((star_data["aperture_sum"][1]), 10)
print(count)
count += 1

mag_garnet = -2.5 * math.log((star_data["aperture_sum"][0]), 10) + zero_point
magnitudes.append(mag_garnet)

zero_point_2 = magnitude_of_hd239746 + 2.5 * math.log((star_data_2["aperture_sum"][1]), 10)
mag_garnet_2 = -2.5 * math.log((star_data["aperture_sum"][0]), 10) + zero_point_2



