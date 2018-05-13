# Setup-Files
The files I use to setup my terminal, emacs, tmux, etc

## To apply terminal theme:
'''
./terminal-theme.sh
'''
- you can also customize the colors by editting the sh file

## To apply emacs configuration:
'''
cp ./.emacs ~/
'''

## To apply Tmux configuration:
'''
cp ./.tmux.conf ~/
tmux source-file ~/.tmux.conf
'''
- read comments in .tmux.conf to see how the configuration works