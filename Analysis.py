import cv2
import numpy as np
from scipy.stats import itemfreq
import matplotlib.pyplot as plt

def AverageColor(frames):
    avg_cols = []
    for frame in frames:
        avg_color_per_row = np.average(frame, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        avg_cols.append(avg_color)

    return avg_cols


def FindOutlierColor(colors):
    print "unimplemented..."
    pass

def PlotColor(colors):
    x = np.average(colors, axis=1)
    y = range(length(colors))
