#!/usr/bin/python

import os, sys

# Open a file
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT|os.O_EXLOCK )

# Write one string
os.write(fd, "This is test")

# Close opened file
os.close( fd )

print("Closed the file")
