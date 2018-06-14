#!/bin/sh

yaourt -Qqtn > yaourt.txt
pip freeze > pip.txt
conda list --export > conda.txt
