# PhotometryPipelineEVCResearchCourse
A pipeline to conduct aperture photometry of variable stars and generate time-series data and measurements. This pipeline is easy to use for introductory photometry, easy to edit due to the astropy implementations, and easy to understand. 

---

# Motivations

Traditionally, aperture photometry is done with a software like APT, which takes `.fit` files one by one, creates a reference, and uses pixel counts to help the user determine the magnitude or flux of a point source in an exposure. This works well for extended point sources or for point sources known to be constant in magnitude, but can be tedious when dealing with time-series data. This pipeline deals with exposures of the same target across days or even months, and returns a light curve of the chosen target, specified by pixel coordinates on the image. It calculates magnitude through input of a reference star and its known magnitude. 

This program uses astropy to calculate pixel counts, and conducts differential photometry to calculate magnitude, given a zero-point input. The outputted images can be easily stretched or edited otherwise, and apertures can be easily edited as well due to the astropy implementation in the code. 

# Usage

`main.py` contains code that takes processed `.fit` files, uses the reference's magnitude and zero-point to conduct differential photometry and return a light-curve. Other modules within the astropy or gatspy implementation can be used for further time-series analysis. 

The `apertures` folder contains examples of the subexposures as displayed in matplotlib with the fitted apertures. These can be edited through the code as desired. 
