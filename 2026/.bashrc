# Dim the white text on virtual consoles (TTYs) so it's not blinding
if [ "$TERM" = "linux" ]; then
    printf '\e]P7553300'
fi

if [[ -z "$TMUX" ]]; then
    tmux
fi

bash -c "xmodmap ~/.xmodmap &>/dev/null &"

alias emacs="emacs -nw"
alias d="source d"
alias f="d; echo \"---\";git status"
alias ls="ls --color=always"
alias grepc="grep --color=always"
alias dm="diffman"
alias nightshift="redshift -P -O 3300"
alias midshift="redshift -P -O 4600"
alias dayshift="redshift -P -O 7000"
alias copy="xclip -selection c"
alias paste="xclip -selection clipboard -o"
alias callers="calls r ."
alias callees="calls e ."
alias gimp="flatpak run org.gimp.GIMP"
alias python="python3"
alias clod="claude --dangerously-skip-permissions"
alias clodl="claude --dangerously-skip-permissions --effort low"
alias clodm="claude --dangerously-skip-permissions --effort medium"
alias clodh="claude --dangerously-skip-permissions --effort high"
alias cv="claude-view"
alias cvu="claude-view start" #up
alias cvd="claude-view stop" #down
alias eb="eyeball"
alias clos="claude --dangerously-skip-permissions --model sonnet --effort medium"
alias cloh="claude --dangerously-skip-permissions --model haiku"
alias clok="claude --dangerously-skip-permissions --model haiku"

#eval $(thefuck --alias)


export OPENAI_API_KEY="$(cat ~/.keys/.open_ai)"

export GCP_VM="35.225.197.68"

export PATH="$PATH:$HOME/bin"
export PATH="$PATH:$HOME/.local/bin"
export PATH="$PATH:/home/linuxbrew/.linuxbrew/bin"

export BASE_DIR=$(cd ~; pwd)
. "$HOME/.cargo/env"
export PATH="$HOME/.cargo/bin:$PATH"

## colors ##
# prompt
#export PS1='\[\e[1;33m\]\u@\h\[\e[0m\]:\[\e[37m\]\w\[\e[1;35m\]\$\[\e[0m\] '
export PS1='\[\e[1;33m\]\u\[\e[0m\]:\[\e[37m\]\w\[\e[1;35m\]\$\[\e[0m\] '



# autocompletions
for file in ~/bin/complete_*; do
    if [ -f "$file" ]; then
        source "$file"
    fi
done

# history
export HISTSIZE=5000
export HISTFILESIZE=10000
shopt -s histappend
PROMPT_COMMAND="history -a;$PROMPT_COMMAND"

## written by GCP install $$
# The next line updates PATH for the Google Cloud SDK.
if [ -f '/home/weston/installs/google-cloud-sdk/path.bash.inc' ]; then . '/home/weston/installs/google-cloud-sdk/path.bash.inc'; fi
# The next line enables shell command completion for gcloud.
if [ -f '/home/weston/installs/google-cloud-sdk/completion.bash.inc' ]; then . '/home/weston/installs/google-cloud-sdk/completion.bash.inc'; fi



export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion


gfx_prgm=glxgears

# temporary mutter workaround
#if [[ -z $(ps aux | grep $gfx_prgm | grep -v grep) ]]; then
#    echo $(nohup $gfx_prgm &>/dev/null) &
#    sleep 1
#    winID=$(xdotool search $gfx_prgm)
#    xdotool windowsize $winID 20 20
#    xdotool windowmove $winID 940 0
#    wmctrl -i -r $winID -b add,above
#fi



alias gs="git status"
alias gc="git commit"
alias gp="git push"
alias gco="git checkout"
alias ga="git add"
alias gd="git diff"
alias gpl="git pull"
alias gl="git log"

eval "$(thefuck --alias)"

export PATH="$HOME/llm_bin:$PATH"
