fpath=($ZDOTDIR/external $fpath)

source "$XDG_CONFIG_HOME/zsh/aliases"

zmodload zsh/complist

autoload -Uz compinit; compinit 
_comp_options+=(globdots) # With hidden files 
source ~/Dotfiles/zsh/external/completion.zsh

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

autoload -Uz prompt_purification_setup; 
prompt_purification_setup

# Push the current directory visited on to the stack.
setopt AUTO_PUSHD
# Do not store duplicate directories in the stack
setopt PUSHD_IGNORE_DUPS
# Do not print the directory stack after using
setopt PUSHD_SILENT

bindkey -v export KEYTIMEOUT=1

autoload -Uz cursor_mode && cursor_mode

autoload -Uz edit-command-line 
zle -N edit-command-line 
bindkey -M vicmd v edit-command-line


if [ $(command -v "fzf") ]; then
	source /usr/share/fzf/completion.zsh 
	source /usr/share/fzf/key-bindings.zsh
fi

if [ "$(tty)" = "/dev/tty1" ]; then
    pgrep i3 || exec startx "$XDG_CONFIG_HOME/X11/.xinitrc"
fi


# PYWAL
#
# Import colorscheme from 'wal' asynchronously & # Run the 
# process in the background. ( ) # Hide shell job control 
# messages. Not supported in the "fish" shell.
(cat ~/.cache/wal/sequences &)

# Alternative (blocks terminal for 0-3ms)
cat ~/.cache/wal/sequences

# To add support for TTYs this line can be optionally added.
source ~/.cache/wal/colors-tty.sh

# Needed for pywal
export PATH="/home/antharia/.local/bin:$PATH"

# Go installation
export PATH=$PATH:/usr/local/go/bin

# Charm
export CHARM_HOST=localhost

# VST
export VST3_PATH="$VST3_PATH:/usr/lib64/vst3:/home/antharia/.wine/drive_c/Program Files/Common Files/VST3:/home/antharia/.vst3/yabridge"

# Golang
export GOPATH=$HOME/.config/go
export PATH=$PATH:/usr/local/go/bin

# Cursor theme
export XCURSOR_THEME=bibata-cursor-theme

# export MESA_GL_VERSION_OVERRIDE=3.3

# Zoxide
eval "$(zoxide init zsh)"

