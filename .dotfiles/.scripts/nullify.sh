#!/bin/bash

# Global Variables
GENERAL=(".xsession_errors")
HISTORIES=(".bash_history" ".zsh_history")
NULL=/dev/null

# Functions
link () {
  INPUT="$@"
  for FILE in ${INPUT[@]}; do
    TARGET=$HOME/$FILE
    ln -f -s $NULL $TARGET && echo "Linked $TARGET -> $NULL";
  done
}

unlink () {
  ARR="$@"
  for FILE in ${INPUT[@]}; do
    TARGET=$HOME/$FILE
    unlink $TARGET && echo "Unlinked $TARGET";
  done
}

# Main()
link ${GENERAL[@]}

if [ "$1" = "history" ]; then
  link ${HISTORIES[@]};
fi

if [ "$1" = "unlink" ]; then
  unlink ${GENERAL[@]}
  unlink ${HISTORIES[@]}
fi
