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

#import our hellosikuliworld.py file.
#hellowsikuliworld.py will be the actual logic that uses sikuli to interact with our testApp
import hellosikuliworld

#Call our hellosikuliworld function in a thread to interact with the testApp
hellosikuliworldThread = threading.Thread(target=hellosikuliworld.interactTestApp)
hellosikuliworldThread.start()

#Before we exit our main thread/function, let's bring back in our sikuli thread
#before we close out and exit.  This will prevent any further logic from executing until
#the hellosikuliworldThread finishes
hellosikuliworldThread.join()

#Print a message before the script ends
print('Main Function Finished')
