#!/bin/bash

x=$1

for (( i=1; i <= $x; ++i ))
do
	for (( j=$x; j >= $i; j-- ))
	do
		echo -ne " "
	done
	for (( n=1; n <= $i; ++n ))
	do
		echo -ne "* "
	done
	echo -e "\n"
done

x=$((x -1 ))
for (( i=1; i <= $x; ++i ))
do
	for (( j=1; j <= $i; j++ ))
	do
		echo -ne " "
	done
	for (( n=$x; n >= $i; n-- ))
	do
		echo -ne " *"
	done
	echo -e "\n"
done
