import cv2
import sys
from cvzone.HandTrackingModule import HandDetector
from time import sleep

cap =cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
finalText=""

detector =HandDetector(detectionCon=0.8)
keys=[["Q","w","E","R","T","Y","U","I","O","P"],
["A","S","D","F","G","H","J","K","L",";"],
["Z","X","C","V","B","N","M",",",".","/"]]
def drawAll(img,buttonList):
    for button in buttonList:
        x,y=button.pos 
        w,h=button.size   
        cv2.rectangle(img,button.pos,(x+w,y+h),(255,0,253),cv2.FILLED)
        cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
    return img    

class Button():
    def __init__(self,pos,text,size=[85,85]):
        self.pos=pos
        self.size=size
        self.text=text

    
         

buttonList=[]
for i in range(len(keys)):
    for j,key in enumerate(keys[i]):
        buttonList.append(Button([100*j+5,100*i+50],key))
   

while True:
    success,img=cap.read()
    img= detector.findHands(img)
    lmlist,bboxInfo=detector.findPosition(img)
    # crete rectangles for keys
    img=drawAll(img,buttonList)

    if lmlist:        #hand is there
        for button in buttonList:
            x,y=button.pos
            w,h=button.size
            if x<lmlist[8][0]<x+w and y<lmlist[8][1]<y+h:
                cv2.rectangle(img,button.pos,(x+w,y+h),(155,0,200),cv2.FILLED)
                cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
            l,_,_=detector.findDistance(8,12,img)   

            if l<30:  
                 cv2.rectangle(img,button.pos,(x+w,y+h),(255,0,0),cv2.FILLED)
                 cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)  
                 finalText+=button.text            
    

    cv2.rectangle(img,(50,350),(700,450),(255,255,255),cv2.FILLED)
    cv2.putText(img,finalText,(60,425),cv2.FONT_HERSHEY_PLAIN,5,(0,0,0),4)              

    cv2.imshow("IMAGE",img)
    cv2.waitKey(1)


