#HelloWorld Example in Sikuli by XAsmodeaNX
#
#This script will search our testApp for the OK button and click it.
#This is not a regular python script, it is a Jython script meant to be called from _main.py
#

#Sikuli Function Documentation: https://sikulix-2014.readthedocs.io/en/latest/scripting.html
#Common Sikuli Functions: 
############FINDING
#find(image.png)
#findAll(img.png)
#wait(img.png)
#waitVanish(image.png)
#exists(img.png)
#Import any python libraries we might find necessary
#############MOUSE ACTIONS
#click(img.png)
#doubleClick(img.png)
#rightClick(img.png)
#hover(img.png)
#dragDrop(img1.png, img2.png)
#############KEYBOARD ACTIONS
#https://sikulix-2014.readthedocs.io/en/latest/textandocr.html
#type(string)
#type(img.png, string)
#paste(string)
#paste(img.png, string)
#############EVENT OBSERVATION
#onAppear(img.png, hnd)
#onVanish(img.png, hnd)



import sys; 
import time;
import threading;
import logging

#Import our Jython libraries from Sikuli
import org.sikuli.script.SikulixForJython
import org.sikuli.script.ImagePath
import org.sikuli.script.OCR

#Import the sikuli classes
from sikuli import *

def interactTestApp():
    #Since we are in a standalone jython/python script, we need to tell sikuli
    #that our Image path is not necessary in the same folder as this running file.
    #Since our images will be in an images subfolder, we need to tell Sikuli how 
    #to find them here and add it to the Sikuli ImagePath
    ImagePath.setBundlePath("images")
    
    #We can verify now that our sikuli ImagePath now contains the images folder
    #where our images are held for this exercise
    imgPath = getImagePath()
    for p in imgPath:
            print p
            
    
    #Grab the sikuli Screen object so that sikuli becomes aware of the screen.  
    #Note that this is less like a screenshot, a more like a continuous video of the screen.
    #Note here that we are going to search the ENTIRE screen.  It is possible to only search a subregion if you know
    #that your image will always appear in the same region.  Searching the entire screen can be SLOW
    s=Screen()
    
    #Get our MoveMouseDelay, i.e. the time it takes for the mouse to move to a target in the screen.
    #A delay of zero means the mouse "jumps" to the target immediately. Default is 0.5
    mmd = Settings.MoveMouseDelay # save default/actual value
    print("Starting mouse delay: ", mmd)
    Settings.MoveMouseDelay = 5
    nmmd = Settings.MoveMouseDelay
    print("Set new mouse delay: ", nmmd)
    
    #We can draw images on the screen of what Sikuli is doing, this is very helpful to debug what it is actually doing
    #Note: setShowActions(True) will override our mouse settings and use the defaults for everything!
    setShowActions(True)
    
    btnText = OCR.readText("1080p_testApp_btn_OK.PNG")
    print("btnText was: " + btnText)
    
    
    #Search the screen object for our image and click it if found.  We are setting the OpenCV similarity index here to 95% (default is 70%)
    #and our click location will be offset from the center of the found image by (x,y), (-8,33), E.g. Left and Down
    #Note that the x,y coordinates in Sikuli are as follows: -x = LEFT, +x = right, -y=UP, y=DOWN.
    ##A word on images:  Images that sikuli/OpenCV uses to try and find, MUST have been pre-collected on a screen with
    ##the SAME RESOLUTION as the screen being searched.  In other words, DO NOT grab screenshots on your big 4k monitor
    ##and then expect them to work when Sikili is working in a screen of 1920x1080.  This is CRITICAL.
    ##The most reliable way to collect screenshots and set similarity/offsets is to use the SikuliXide jar, then rename the
    ##file to something that makes sense to you and move it into our images folder
    s.click(Pattern("1080p_testApp_btn_OK.PNG").similar(0.95).targetOffset(-8,33))
    return None
