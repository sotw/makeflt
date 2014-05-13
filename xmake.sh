cp ~/bin/makeflt.py ./
make $1 2>&1 | python makeflt.py 1 1
rm makeflt.py
