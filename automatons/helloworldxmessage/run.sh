#!/bin/bash

JAVABIN=`which java`
if [ "$?" != "0" ]; then
  echo "Please install java!"
  exit 1
fi

if [ ! -f sikulixide-2.0.5.jar ]; then
  wget https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixide-2.0.5.jar
fi

if [ ! -f sikulixapi-2.0.5.jar ]; then
  wget https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixapi-2.0.5.jar
fi

xmessage -buttons ClickMeAutomatically "Hello World" &
${JAVABIN} -jar sikulixapi-2.0.5.jar -r _main.py
