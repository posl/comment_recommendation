def swap(L, i, j):
    temp = L[i:j+1]
    temp.reverse()
    L[i:j+1] = temp
