#!/bin/bash

if [ -f ldd_libs.txt ]
then
    rm ldd_libs.txt
fi

# Gets list of commands to test (one per line)
ls /usr/bin | awk 'NR%101==704598596%101' > commands.txt

# For every command run ldd on it. The outputted dynamic libraries can be redirected to the end of ldd_libs.txt
while read command
do
    ldd /usr/bin/$command >> ldd_libs.txt
done < commands.txt

# Substitutes the addresses with zilch, => isn't in every line
sed -i 's/(0x0.*//' ldd_libs.txt
# Deletes the error message
sed -i '/not a dynamic executable/d' ldd_libs.txt
# Sorts the list uniquely
sort -u ldd_libs.txt > sorted_libs.txt

echo "Success?!"
