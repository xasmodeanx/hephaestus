#HelloWorld Example in Sikuli by XAsmodeaNX
#
#This script will open a test application and use Sikuli to find a button
#and click it, thus ending the program.
#This is not a regular python script, it is a Jython script meant to be called from the SikuliXapi.
#
#To run this script: java -jar /path/to/sikuliXapi.jar -r _main.py

#Import any necessary or useful python/jython libraries
import sys; 
import time;
import threading;
import logging


#We want to import another script with the filename of testApp.py
#testApp.py will launch a simple GTK window so that we can practice Sikuli on a predictable target
#Note that testApp.py MUST BE IN THE SAME FOLDER as the script that is 
#trying to import it.  I am not python smart enough to figure out how to import
#a python script that isn't in the same directory... maybe one day
import testApp

#import our hellosikuliworld.py file.
#hellowsikuliworld.py will be the actual logic that uses sikuli to interact with our testApp
import hellosikuliworld

#We are defining a variable that we will pass to our testApp later
#Note that python/jython is not strongly typed so we have no variable type
myNameString="Jason"

#We can define an inline function here that will launch our testApp in a background
#Thread.  This will allow the testApp to fire up and run without blocking 
#execution of the rest of this exercise.  This thread will run until it finishes
#or python/jython is terminated.  
def launch_testApp_in_backgroundThread():
    testAppThread = threading.Thread(target=testApp.function_open_helloworld_window, args=(myNameString,))
    testAppThread.start()
    return None
#Go ahead and call our function to launch testApp in the background
launch_testApp_in_backgroundThread()
#Give the testApp a second to launch
time.sleep(1)

#Call our hellosikuliworld function in a thread to interact with the testApp
hellosikuliworldThread = threading.Thread(target=hellosikuliworld.interactTestApp)
hellosikuliworldThread.start()


#Before we exit our main thread/function, let's bring back in our sikuli thread
#before we close out and exit.  This will prevent any further logic from executing until
#the hellosikuliworldThread finishes
hellosikuliworldThread.join()

#Print a message before the script ends
print('Main Function Finished')