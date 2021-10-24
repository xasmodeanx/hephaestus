# Hephaestus - SikuliX Automatons

## What is Hephaestus?
Hephaestus was the Greek god of blacksmiths.  
Hephaestus crafted much of the magnificent equipment of the gods, and almost any finely wrought metalwork imbued with powers that appears in Greek myth is said to have been forged by Hephaestus. 
He designed Hermes' winged helmet and sandals, the Aegis breastplate, Aphrodite's famed girdle, Agamemnon's staff of office, Achilles' armour, Diomedes' cuirass, Heracles' bronze clappers, Helios' chariot, the shoulder of Pelops, and Eros's bow and arrows. 
In later accounts, Hephaestus worked with the help of the Cyclopes, among them his assistants in the forge, Brontes, Steropes and Arges.

_**Hephaestus built automatons of metal to work for him.**_

This repository contains automatons, aka SikuliX automation routines for specific applications.  

### Check out the [hellosikuliworld](https://github.com/xasmodeanx/hephaestus/tree/main/automatons/hellosikuliworld) automaton for a primer and example of what can be done and how.

![hippo](https://thumbs.gfycat.com/UltimateOccasionalAustraliankestrel-size_restricted.gif)

## What is Sikuli/SikuliX?
Sikuli/SikuliX is a  Black Box GUI testing tool. 
Sikuli allows you to comprehensively test applications, by allowing you to simulate user-inputs to any software that has a visual component.
Sikuli uses image recognition via the OpenCV (Computer Vision) libraries and OCR via the Tesseract (Tess4J) and Leptonica libraries.
Users can use the Sikuli IDE or Eclipse/Netbeans to create Sikuli-formatted python/jython scripts, which can be executed as tests against anything that can appear on the screen.

## Pre-requisites
1. Download [SikuliXide*.jar](https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixide-2.0.5.jar) and [SikuliXapi*.jar](https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixapi-2.0.5.jar) for your OS and place them in this directory. 
Note: This repository was written and tested with SikuliX 2.0.5.
2. Prepare your environment by installing the Tesseract OCR libraries 
`sudo apt install libtesseract4` 
Note: Sikuli requires libtesseract > 4.1.x
3. Install OpenJDK-11
`sudo apt install openjdk-11-jre`
4. Some automatons may have their own dependencies, see the automaton folder you are interested in for more information.
 
## Running a Hephaestus automaton
`cd automatons/hellosikuliworld/; ./run.sh`


