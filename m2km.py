#
# Write a program to change miles into
# kilometers
# and let people type in the miles
# they want to change
#
# stretch if time - round the answer to 2 decimal places
#

# input the miles (from keyboard)
m = input("How many miles ")


# convert to a number
m = float(m)


# calculate the number of km
k = m * 1.6


# print the answer
print(m, "miles is", round(k,2), "km")
