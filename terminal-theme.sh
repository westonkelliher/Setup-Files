#!/bin/bash

#stolen from https://gist.github.com/matiasleidemer/24a32d80e8409984557e

echo
echo "This script sets the pantheon terminal to Weston's Theme; Customize it if you like."
echo



bg_dark='rgba(6,8,10,1)'
fg_white='rgba(240,245,240,1)'
cursor_green='rgba(130,250,130,1)'
solarized_palette='#070736364242:#DCDC32322F2F:#858599990000:#B5B589890000:#26268B8BD2D2:#D3D336368282:#2A2AA1A19898:#EEEEE8E8D5D5:#00002B2B3636:#CBCB4B4B1616:#58586E6E7575:#65657B7B8383:#838394949696:#6C6C7171C4C4:#9393A1A1A1A1:#FDFDF6F6E3E3'

#change '#<hexidecimal>' type value to 'rgba(<red>,<green>,<blue>,1) type values for easy customization



gsettings set org.pantheon.terminal.settings background $bg_dark
gsettings set org.pantheon.terminal.settings foreground $fg_white
gsettings set org.pantheon.terminal.settings cursor-color $base00
gsettings set org.pantheon.terminal.settings palette $solarized_palette
