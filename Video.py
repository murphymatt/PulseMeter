import cv2

import time

def Capture():
    cap = cv2.VideoCapture(0)

    frame_rate = 24
    vid_length = 5
    num_frames = frame_rate * vid_length
    
    start = time.time()

    rets = []
    frames = []
    for i in range(num_frames):
        ret, frame = cap.read()
        rets.append(ret)
        frames.append(frame)
    
    cap.release()
    cv2.destroyAllWindows()

    return rets, frames


def ShowFrames(frames):    
    for frame in frames:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
