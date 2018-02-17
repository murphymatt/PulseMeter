#!/bin/python

from Video import Capture, ShowFrames
from FaceMask import ComputeMask

def main():
    # capture video
    rets, frames = Capture()

    # compute face mask from frames
    frames = ComputeMask(frames)
    ShowFrames(frames)
    
if __name__ == '__main__':
    main()
