#!/bin/bash

#get auth work with polkit-gnome
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# dex execute .desktop files
# keep in mind that it can cause issues 
# when second to i3 a DE is installed or mixed usage of i3 + xfce4 or GNOME
# in this cases better disable dex and use manual starting apps using xdg/autostart
dex -a -s /etc/xdg/autostart/:~/.config/autostart/ &

# num lock activated
#exec --no-startup-id numlockx on

# start conky: 
#exec_always --no-startup-id conky

# start a script to setup displays
# uncomment the next line, use arandr to setup displays and save the file as monitor:
~/.screenlayout/monitor.sh &

# start blueberry app for managing bluetooth devices from tray:
#blueberry-tray &

#transparency 
#exec --no-startup-id xcompmgr -c -C -t-5 -l-5 -r4.2 -o.55 &
picom -CGb &

#networkmanager-applet
nm-applet &

# flux
fluxgui &

# set wallpaper
nitrogen --restore &
#exec --no-startup-id feh --bg-fill /usr/share/endeavouros/backgrounds/endeavouros_i3.png

#set powersavings for display:
xset s 480 dpms 600 600 600 &

# Desktop notifications
dbus-launch dunst --config ~/.config/dunst/dunstrc &

# Autostart apps as you like
#exec --no-startup-id sleep 2 && xfce4-terminal
#sleep 2 && alacritty &
#exec --no-startup-id sleep 7 && firefox https://github.com/endeavouros-team/endeavouros-i3wm-setup/blob/main/force-knowledge.md
#exec --no-startup-id sleep 3 && thunar

# Set brightness to 0.08 when login
xbacklight -set 1 &

# Remove all temp clipboard images
rm /tmp/*.png &
