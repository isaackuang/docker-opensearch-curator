#!/bin/bash

function retag() {
    git push --delete origin $1
    git tag -d $1
    git tag $1
    git push origin $1
}


if [ "$1" != "" ] || [ $# -gt 1 ]; then
    retag $1
else
  echo "Use: $0 <tag-name>"
fi
