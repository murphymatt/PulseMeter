#!/bin/python

from Video import Capture, ShowFrames
from FaceMask import ComputeMask
from Analysis import AverageColor

def main():
    # capture video
    rets, frames = Capture()
    ShowFrames(frames)

    # compute face mask from frames
    (frames, faces) = ComputeMask(frames)
    ShowFrames(faces)

    # compute average color for each face
    avg_cols = AverageColor(faces)
    
    
if __name__ == '__main__':
    main()
