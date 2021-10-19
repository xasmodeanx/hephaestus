# XAsmodeanNX's SikuliX Example Code (HelloSikuliWorld!) as Eclipse or Standalone project

## Pre-requisites
1. Download [SikuliXide*.jar](https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixide-2.0.5.jar) and [SikuliXapi*.jar](https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixapi-2.0.5.jar) for your OS and place them in this directory. 
Note: This repository was written and tested with SikuliX 2.0.5.
2. Prepare your environment by installing the Tesseract OCR libraries 
`sudo apt install libtesseract4` 
Note: Sikuli requires libtesseract > 4.1.x
3. Install OpenJDK-11
`sudo apt install openjdk-11-jre`
 
## Running Example
`java -jar sikuliXapi.jar -r _main.py`

## What is Sikuli/SikuliX?
Sikuli/SikuliX is a  Black Box GUI testing tool. 
Sikuli allows you to comprehensively test applications, by allowing you to simulate user-inputs to any software that has a visual component.
Sikuli uses image recognition via the OpenCV (Computer Vision) libraries and OCR via the Tesseract (Tess4J) and Leptonica libraries.
Users can use the Sikuli IDE or Eclipse/Netbeans to create Sikuli-formatted python/jython scripts, which can be executed as tests against anything that can appear on the screen.

## Code Structure (Learn this example!)
### Don't Judge!
This is my first ever python/jython script and I had to learn a lot to make it work.  So I'm sure there are much better ways to do things...
Like for instance... how do I import .py files for use in my _main.py if the .py files are in different folders?  Let me know...
### _main.py
_main.py is the "main" script which calls all of the rest.  _main.py has some great examples of simple python/jython
concepts such as threading, joining, creating variables, creating function definitions, imports and calling other functions
from other files.  Start here.
### testApp.py
testApp.py is a very simple script to use the SikuliX Jython libraries to open a simple GTK window with an OK button. 
This will be the app that we execute our SikuliX methods on, to control it visually.
### hellosikuliworld.py
hellosikuliworld.py is a small sikuli/python/jython script to interact with the testApp window.  Of note we will be using
the sikuli-built-in OpenCV methods to find an image on the user's screen, then we will move the mouse there and click it.
Keep an eye on what is happening visually and in the terminal output!  We will also be using OCR from libtesseract 4.1.1 (HARD DEPENDENCY)
to read the include .png file of the GTK window and extract text strings from it.

## Other Notes
### Setting up Eclipse for Sikuli Jython Development:
0. Reference this whole thing with http://doc.sikuli.org/faq/040-other-ide.html#eclipse
1. Install Eclipse
2. Install pydev plugin
	a. Eclipse -> Help -> Eclipse Marketplace
	b. Search pydev -> install
3. Create a new pydev project
	a. File -> New -> Project -> pyDev template
	b. Add a helloworld.py file
		import sys; 
		import org.sikuli.script.SikulixForJython
		from sikuli import *
		popup("test", "title")
		print('Hello world! Did this change again?')
	c. Save changes
4. Configure pydev jython interpreter		
	a. Download jython-standalone.2.7.2.jar from maven
	b. Eclipse -> Window -> Preferences -> PyDev -> Interpreters -> Jython Interpreters -> New -> Browse for Jython Jar
	c. Navigate and select jython-standalone-2.7.2.jar
	d. When presented with warning about python stdlib source files not found, you can safely click Proceed Anyway
	e. Accept/Save changes
5. Add the Sikulixapi jar to Jython Environment for Project
	a. Download the SikuliXapi jar file from Launchpad
	b. Eclipse -> Right-click Pydev Project in left-pane -> Properties -> PyDev - PYTHONPATH -> External Libraries -> Add Zip/Jar/Egg -> Navigate and select the SikuliXapi jar
	c. Accept/Save changes 
6. Add the Sikulixapi Lib folder to Jython Environment for Project
	a. Extract the Lib folder from the SikuliXapi jar file
		i. jar -xvf sikuliapi.jar
	b.  Eclipse -> Right-click Pydev Project in left-pane -> Properties -> PyDev - PYTHONPATH -> External Libraries -> Add Source Folder -> Navigate and select the SikuliXapi Lib folder
	c. Accept/Save changes
7. Run the helloworld.py file with Jython
	a. Right click helloworld.py in Pydev Project left-pane -> Run As -> Jython Run
	b. Output should be a GUI window popping up and something written to the console!
	
## KNOWN ISSUES
### Eclipse Code Completion/Autocomplete
Eclipse with Jython has serious issues with Code Completion. Be very careful when using it as it may freeze Eclipse temporarily
while it tries and fails to fetch completion text on some python classes.
### Sikuli fails to find the OK button!
OpenCV/Sikuli are VERY particular about image comparisons and resolutions.  This repository and the screenshot of the GUI window and OK button were done on a default Ubuntu 20.04 desktop at 1080p resolution.  If you aren't in that environment, it might not work due to window theme differences or even screen resolution differences.
		
## Useful links:
### Interaction  with user: 
http://doc.sikuli.org/globals.html#importingsikuliscripts
### Text and OCR
https://sikulix-2014.readthedocs.io/en/latest/textandocr.html
### Scripting/Finding images
https://sikulix-2014.readthedocs.io/en/latest/scripting.html
