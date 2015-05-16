#-------------------------------------------------------------------------------
# Name:             sorting_select
# Purpose:          sorting_select(using exec keyword)
#-------------------------------------------------------------------------------

func = {1:'bubblesort', 2:'insertionsort', 3:'selectionsort'}

i = input('please input number(1-bubblesort, 2-insertionsort 3-selectionsort)')

if i not in func:
    print 'invalid input'
else:
    exec 'import %s' % func[i]