#!/bin/bash

#stolen from https://gist.github.com/matiasleidemer/24a32d80e8409984557e

echo
echo "This script sets the pantheon terminal to Weston's Theme; Customize it if you like."
echo



bg_dark='rgba(6,8,10,1)'
fg_white='rgba(240,245,240,1)'
fg_gray='rgba(200,205,200,1)'
green_brit='rgba(130,250,130,1)'
blue_dk='rgba(50,50,100,1)'
turq_p='rgba(50,200,80,1)'

color0='#070736364242:'
color1='#DCDC32322F2F:'
color2='#858599990000:'
color3='#B5B589890000:'
color4='#58586E6E7575:'
color5='#D3D336368282:'
color6='#2A2AA1A19898:'
color7='rgba(50,50,100,1):'
color8='#00002B2B3636:'
color9='#CBCB4B4B1616:'
color10='rgba(50,200,80,1):'
color11='rgba(30,150,60,1):'
color12='#26268B8BD2D2:'
color13='#6C6C7171C4C4:'
color14='#9393A1A1A1A1:'
color15='#9393A1A1A1A1:'


palette=$color0$color1$color2$color3$color4$color5$color6$color7$color8$color9$color10$color11$color12$color13$color14$color15

#change '#<hexidecimal>' type value to 'rgba(<red>,<green>,<blue>,1) type values for easy customization



gsettings set org.pantheon.terminal.settings background $bg_dark
gsettings set org.pantheon.terminal.settings foreground $fg_gray
gsettings set org.pantheon.terminal.settings cursor-color $base00
gsettings set org.pantheon.terminal.settings palette $palette
