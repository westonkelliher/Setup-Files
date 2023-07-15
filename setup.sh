#!/bin/bash


sudo apt install emacs tmux
cp .bashrc ~/
cp .emacs ~/
cp .tmux.conf ~/
tmux source-file ~/.tmux.conf
cp .xmodmap ~/
xmodmap ~/.xmodmap

cp -r bin ~/


echo "xmodmap setup may not work to disable caps lock if you are on ubuntu"
echo ""
read -p "Install gnome-tweaks to unset caps via GUI? (y/n)" response

if [[ $response == "y" ]]; then
    sudo apt install gnome-tweaks
    echo ""
    echo "Keyboard & Mouse > Keyboard > Additional Layout Options > Caps Lock "
    echo "behavior."
    gnome-tweaks
fi
