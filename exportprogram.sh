#!/bin/sh

yaourt -Qqtn > yaourt.txt
pip freeze > pip.txt
conda list --export --no-pip > conda.txt
