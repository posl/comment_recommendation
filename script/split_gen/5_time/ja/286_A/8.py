def swap(array, p, q, r, s):
    tmp = array[p-1:q]
    array[p-1:q] = array[r-1:s]
    array[r-1:s] = tmp
    return array
