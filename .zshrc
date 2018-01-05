source /etc/zsh/zpreztorc
source /usr/lib/prezto/init.zsh
source /usr/lib/prezto/runcoms/zshrc

autoload -Uz promptinit
promptinit
prompt cloud

export PATH=/home/kevin/.local:/opt/anaconda/bin:$PATH
export HISTFILE=~/.zsh_history
export HISTSIZE=500
export SAVEHIST=500
