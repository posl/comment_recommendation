def swap_array(array, p, q, r, s):
    array1 = array[:p-1]
    array2 = array[p-1:q]
    array3 = array[q:r]
    array4 = array[r:s]
    array5 = array[s:]
    return array1 + array3 + array2 + array5 + array4
