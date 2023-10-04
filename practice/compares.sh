#!/bin/bash
#compares $1 and $2

if [$1 -gt $2 ];
then
    echo "the first number is greater than the second number"
elif [ $1 -lt $2 ];
then
    echo "the second number is greater than the first"
else
    echo "the two number are equal"
fi          