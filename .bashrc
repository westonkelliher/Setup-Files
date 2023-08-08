# custom (by weston)

xmodmap ~/.xmodmap

alias emacs="emacs -nw"
alias d="source d"
alias ls="ls --color=always"

export PATH="$PATH:~/bin"

export BASE_DIR=$(cd ~; pwd)
. "$HOME/.cargo/env"

# autocompletions
for file in ~/bin/complete_*; do
    if [ -f "$file" ]; then
	source $file
    fi
done

# history
export HISTSIZE=5000
export HISTFILESIZE=10000
shopt -s histappend
PROMPT_COMMAND="history -a;$PROMPT_COMMAND"
