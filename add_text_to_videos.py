import cv2
import datetime


cap = cv2.VideoCapture(0)

#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cap.set(cv2.CAP_PROP_FRAME_WIDTH,333)     #3 for width
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,333)      #4 for height

#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'Width: ' + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + ' height: ' + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.resizeWindow("framename", 1208, 720)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()