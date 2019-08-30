#!/usr/bin/env python
"""Download example."""

import ee
import ee.mapclient

ee.Initialize()

# Get a download URL for an image.
image1 = ee.Image('CGIAR/SRTM90_V4')
path = image1.getDownloadUrl({
    'scale': 30,
    'crs': 'EPSG:4326',
    'region': '[[7.039110171106358,38.36887597284253],[11.082078921106358,38.36887597284253],[11.082078921106358,43.4940539728663],[7.039110171106358,43.4940539728663],[7.039110171106358,38.36887597284253]]'
,'maxPixels': 1e15})
print (path)
