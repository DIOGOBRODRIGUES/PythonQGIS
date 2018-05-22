import sys 
import numpy as np
import matplotlib.pyplot as plt
from qgis.analysis import QgsZonalStatistics

canvas=qgis.utils.iface.mapCanvas()

layers=canvas.layers()
layers[0].name()

layers[1].name()

for x in range(366):
	zoneStat = QgsZonalStatistics (layers[0], layers[1], '_', x, QgsZonalStatistics.Mean)
	zoneStat.calculateStatistics(None)
