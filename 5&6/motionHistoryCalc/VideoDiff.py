import cv2
import numpy
import time
from matplotlib import pyplot
from numpy import arange
import bisect

def scatterplot(x,y):
    pyplot.plot(x,y,'b.')
    pyplot.xlim(min(x)-1,max(x)+1)
    pyplot.ylim(min(y)-1,max(y)+1)
    pyplot.xlabel('Frame No.')
    pyplot.ylabel('Movement')
    pyplot.show()

movement = []

cv2.namedWindow("My Window")

video = cv2.VideoCapture('output.mp4')

successFlag, frame = video.read()

lastFrame = frame.copy()

h, w = frame.shape[:2]
motionHistory = numpy.zeros((h, w), numpy.float32)

while 1:
    successFlag, frame = video.read()

    if not successFlag:
        break

    frameDiff = cv2.absdiff(lastFrame, frame)
    greyDiff = cv2.cvtColor(frameDiff, code=cv2.COLOR_BGR2GRAY)

    retval, motionMask = cv2.threshold(greyDiff,10,1,cv2.THRESH_BINARY)

    timestamp = time.clock()
    cv2.updateMotionHistory(motionMask, motionHistory, timestamp, 0.5) #Updates the motion history image by a moving silhouette.
    mg_mask, mg_orient = cv2.calcMotionGradient( motionHistory, 0.25, 0.05, apertureSize=5 ) #to calculate gradient orientation of a motion history image at each pixel.
    seg_mask, seg_bounds = cv2.segmentMotion(motionHistory, timestamp, 0.25) #Splits a motion history image into a few parts corresponding to separate independent motions

    #print motionHistory

    total = sum(sum(motionHistory))/8
    movement.append(total)

    cv2.imshow("My Window", motionHistory)
    c = cv2.waitKey(7) % 0x100
    if c == 27:
        break

    lastFrame = frame.copy()

xindex = range(len(movement))
scatterplot(xindex, movement)
#print movement, xindex
