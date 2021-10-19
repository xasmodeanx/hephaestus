import sys 
import threading
import time
import logging


import org.sikuli.script.SikulixForJython
from sikuli import *


def function_open_helloworld_window(myName):
    print("Opening Window, " + myName)
    #Call the popup method, a sikuli function that opens a simple GTK window with a single button
    #popup("title", "message")
    popup("Hello", "Hello World!")
    print("Closing Window, " + myName)
    #Return nothing, i.e. this was a void function
    return None
