source /etc/zsh/zpreztorc
source /usr/lib/prezto/init.zsh
source /usr/lib/prezto/runcoms/zshrc

autoload -Uz promptinit
promptinit
prompt agnoster

export CONDA_PATH=/opt/Anaconda
export ANDROID_PATH=/opt/android-sdk/platform-tools:/opt/android-sdk/tools:/opt/android-sdk/tools/bin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl
export PATH=/opt/bin:/opt/cuda/bin:/opt/Anaconda/bin:$ANDROID_PATH:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/cuda/lib64
export HISTFILE=~/.zsh_history
export HISTSIZE=500
export SAVEHIST=500
export BETTER_EXCEPTIONS=1
export SUDO_EDITOR=kate

source activate py37
#ssh alias

alias sshto140='ssh -p 22301 zero2ipo@58.68.234.140'
alias sshto134='ssh -p 22993 root@58.68.234.134'
alias sshto94="ssh -p '22' 'root@58.68.246.94'"
alias sshto250="ssh -p '22' 'root@172.168.17.250'"
alias sshtonw134="ssh -p '22' 'zero2ipo@172.168.11.134'"

alias sshtokvmdc3='ssh -p 28777 root@solarck.top'
alias sshtokvmdc8='ssh -p 28777 root@lunarch.top'
alias sshtovirmach='ssh root@chenwrt.top'

alias cclear='find ~/.cache/ -type f -atime +10 -delete'
alias setproxy="export ALL_PROXY=socks5://127.0.0.1:65509"
alias unsetproxy="unset ALL_PROXY"
alias myip="curl -i http://ip.cn"
