#!/bin/bash

var=0
for filename in *.py; do
	if [ "$filename" != "__init__.py" ]; then
		echo 
		echo "Test $var: $filename"
		echo 
		python3 $filename -v
		var=$(expr $var + 1)
	fi
done