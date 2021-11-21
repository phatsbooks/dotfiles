#!/usr/bin/env bash

scrot /tmp/1-screenshot.png
PICTURE=/tmp/1-screenshot.png

BLUR="5x4"

$SCREENSHOT
convert $PICTURE -blur $BLUR $PICTURE
i3lock -i $PICTURE
rm $PICTURE
