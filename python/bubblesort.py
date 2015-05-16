#-------------------------------------------------------------------------------
# Name:        bubble sort
# Purpose:     sorting test
#-------------------------------------------------------------------------------

import random as r

array = []
for i in xrange(0,50):
    array.append(r.randint(1,100))

print array

for i in xrange(49,-1,-1):
    for j in xrange(i-1,-1,-1):
        if cmp(array[j],array[i])>0:
            #cmp(x,y) if x<y return negative, elif x==y return zero
            #elif x>y return positive
            #swap(array[j],array[i])
            array[j], array[i] = array[i], array[j]

print array