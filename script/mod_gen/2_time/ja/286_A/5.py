def swap_array(array, p, q, r, s):
    array[p-1:q], array[r-1:s] = array[r-1:s], array[p-1:q]
    return array

if __name__ == '__main__':
    swap_array()