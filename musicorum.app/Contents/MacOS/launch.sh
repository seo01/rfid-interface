#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
MEDIA=$(stat -f %N ~/Documents/MusicorumMedia)


python $DIR/musicorum.py --mdir=$MEDIA