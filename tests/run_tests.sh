#!/bin/bash
#echo "python3 capture_output_unittest.py -v"
#python3 capture_output_unittest.py -v

((var++))
for filename in *.py; do
	if [[ $filename != __* ]]; then
		echo "\n"
		echo "Test $var: $filename"
		echo "\n"
		python3 $filename -v
		((var++))
	fi
done