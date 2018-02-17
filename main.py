#!/bin/python

from Video import Capture, ShowFrames
from FaceMask import ComputeMask

def main():
    # capture video
    rets, frames = Capture()
    ShowFrames(frames)

    # compute face mask from frames
    ComputeMask(frames)
    
if __name__ == '__main__':
    main()
