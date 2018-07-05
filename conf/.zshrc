source /etc/zsh/zpreztorc
source /usr/lib/prezto/init.zsh
source /usr/lib/prezto/runcoms/zshrc

autoload -Uz promptinit
promptinit
prompt agnoster

export CONDA_PATH=/opt/Anaconda3
export ANDROID_PATH=/opt/android-sdk/platform-tools:/opt/android-sdk/tools:/opt/android-sdk/tools/bin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl
export PATH=/opt/bin:/opt/cuda/bin:/opt/Anaconda3/bin:$ANDROID_PATH:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/cuda/lib64
export HISTFILE=~/.zsh_history
export HISTSIZE=500
export SAVEHIST=500
export BETTER_EXCEPTIONS=1
export SUDO_EDITOR=kate

#ssh alias

alias sshto140='ssh -p 22301 zero2ipo@58.68.234.140'
alias sshto134='ssh -p 22993 root@58.68.234.134'

alias sshtokvmq='ssh -p 28777 root@solarck.top'
alias sshtokvmcn2='ssh -p 28777 root@lunarch.top'
alias sshtoovzq='ssh -p 28101 root@chenwrt.top'

