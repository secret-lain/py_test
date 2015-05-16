#-------------------------------------------------------------------------------
# Name:        selection sort
# Purpose:     selection sorting test
#-------------------------------------------------------------------------------

import random as r

array = []
for i in xrange(0,50):
    array.append(r.randint(1,100))

print array

for i in xrange(0,49):
    c = i
    for j in xrange(i+1,50):
        if array[c] > array[j]: c = j
    array[i], array[c] = array[c], array[i]

print array