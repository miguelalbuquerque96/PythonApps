import pyttsx3
import PyPDF2
book=open('test.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
speaker = pyttsx3.init()
for num in range(0,pages):
    page=pdfreader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()



import cv2


""" 
img=cv2.imread(r'download.jfif')
cv2.imshow('Output',img)
cv2.waitKey(0)

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success,img=cap.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
"""


