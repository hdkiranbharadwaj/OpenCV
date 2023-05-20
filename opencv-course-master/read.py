import cv2 as cv

# Reading Images

#img = cv.imread('D:\Onedrive\Desktop\Python\opencv-course-master\Resources\Photos\cat_large.jpg')
#cv.imshow('Cat',img)
#cv.waitKey(0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Reading Videos
# capture = cv.VideoCapture('D:\Onedrive\Desktop\Python\opencv-course-master\Resources\Videos\dog.mp4')
# #capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()
# cv.waitKey(0)

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Rescale and Resize:
# def rescaleFrame(frame, scale=0.75):
#     width=int(frame.shape[1] * scale)
#     height=int(frame.shape[0] * scale)
#     dimensions=(width,height)
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# img = cv.imread('D:\Onedrive\Desktop\Python\opencv-course-master\Resources\Photos\cat_large.jpg')
# img = rescaleFrame(img, 0.25)
# cv.imshow('Cat',img)
# cv.waitKey(0)

# def changeRes(width,height):
#     capture.set(3,width)
#     capture.set(4,height)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

