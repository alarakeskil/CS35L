#!/usr/bin/python

# Get in decimals
# Xor it with 42
# Convert to Octal
# Print

# Script to print the necessary octal #s

output = ''

# For every ASCII value
for i in range(0,256):
  # Xor it with 42, convert to octal, convert to int to get rid of leading 0s, convert to string for zfill
  xor = str(int(oct( i ^ 42 )))
  # Makes input string 3 digits long (using leading 0s)
  xor = xor.zfill(3)
  # Append to output string
  output += "\\" + xor

print output
