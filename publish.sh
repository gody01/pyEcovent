#!/bin/bash
#

alias python=python3.10

python3.10 -m twine check  dist/*

if [ $? == 0 ]; then 
 python3.10 -m twine upload  dist/*
fi

