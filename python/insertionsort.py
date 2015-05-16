#-------------------------------------------------------------------------------
# Name: insertion sort
# Purpose: insertion sorting test
#-------------------------------------------------------------------------------

import random as r

array = []
for i in xrange(0,50):
    array.append(r.randint(1,100))


print array

for i in xrange(1,50):
    j = i
    temp_value = array[i]
    while temp_value < array[j-1] and j>0:
        array[j] = array[j-1]
        j -= 1
    array[j] = temp_value

print array