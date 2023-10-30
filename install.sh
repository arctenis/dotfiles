#!/bin/bash

# nvim
mkdir -p "$HOME/.config/nvim"
mkdir -p "$HOME/.config/nvim/undo"
ln -sf "$HOME/Dotfiles/nvim/init.vim" "$HOME/.config/nvim"
rm -rf "$HOME/.config/nvim/bundle"
ln -s "$HOME/Dotfiles/nvim/bundle" "$HOME/.config/nvim"
rm -rf "$HOME/.config/nvim/coc-settings.json"
ln -sf "$HOME/Dotfiles/nvim/coc-settings.json" "$HOME/.config/nvim"

# Xresources
rm -rf "$HOME/.config/X11"
ln -s "$HOME/Dotfiles/X11" "$HOME/.config"

# i3
rm -rf "$HOME/.config/i3"
ln -s "$HOME/Dotfiles/i3" "$HOME/.config"

# zsh
mkdir -p "$HOME/.config/zsh"
ln -sf "$HOME/Dotfiles/zsh/.zshenv" "$HOME"
ln -sf "$HOME/Dotfiles/zsh/.zshrc" "$HOME/.config/zsh"
ln -sf "$HOME/Dotfiles/zsh/aliases" "$HOME/.config/zsh/aliases"
rm -rf "$HOME/.config/zsh/external"
ln -sf "$HOME/Dotfiles/zsh/external" "$HOME/.config/zsh"

# polybar
mkdir -p "$HOME/.config/polybar"
ln -sf "$HOME/Dotfiles/polybar/config" "$HOME/.config/polybar"
ln -sf "$HOME/Dotfiles/polybar/launch.sh" "$HOME/.config/polybar"

# alacritty
mkdir -p "$HOME/.config/alacritty"
ln -sf "$HOME/Dotfiles/alacritty/alacritty.yml" "$HOME/.config/alacritty/alacritty.yml"

# rofi
mkdir -p "$HOME/.config/rofi"
ln -sf "$HOME/Dotfiles/rofi/config.rasi" "$HOME/.config/rofi/config.rasi"

# dunst
mkdir -p "$XDG_CONFIG_HOME/dunst"
ln -sf "$HOME/Dotfiles/dunst/dunstrc" "$XDG_CONFIG_HOME/dunst/dunstrc"

# termite
# mkdir -p "$XDG_CONFIG_HOME/termite"
# ln -sf "$DOTFILES/termite/config" "$XDG_CONFIG_HOME/termite/config"

# tmux
# mkdir -p "$XDG_CONFIG_HOME/tmux"
# ln -sf "$DOTFILES/tmux/tmux.conf" "$XDG_CONFIG_HOME/tmux/tmux.conf"

# gtk3
rm $HOME/.config/gtk-3.0/gtk.css
ln -sf "$HOME/Dotfiles/gtk-3.0/gtk.css" "$HOME/.config/gtk-3.0/gtk.css"
