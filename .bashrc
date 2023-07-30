# custom (by weston)

xmodmap ~/.xmodmap

alias emacs="emacs -nw"
alias d="source d"
alias ls="ls --color=always"

export PATH="$PATH:~/bin"

source ~/bin/complete_*

export BASE_DIR=$(cd ~; pwd)
. "$HOME/.cargo/env"


# history
export HISTSIZE=5000
export HISTFILESIZE=10000
shopt -s histappend
PROMPT_COMMAND="history -a;$PROMPT_COMMAND"
