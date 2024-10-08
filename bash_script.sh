#!/bin/bash
#================================================================
# HEADER
#================================================================
# <purpose of this script>
# Copyright (C) <current date> Lisa McBride (github: lisaleemcb)
# Permission to copy and modify is granted under the MIT license
# Last revised <data revised>

# Options:
#   -h, --help    Display this message.
#   -n            Dry-run; only show what would be done.
#

# if you want to have some arg inputs
arg1=$1
arg2=$2
arg3=$3

# check on inputs
if [ $# -ne 3 ]; then
    echo "Please verify the number of arguments passed. Three arguments are required."
    exit 1
fi

# basic for loop
for i in /etc/rc.*; do
  echo "$i"
done
