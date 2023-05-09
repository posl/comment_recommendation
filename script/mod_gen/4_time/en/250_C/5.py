def swap(i, a):
    tmp = a[i]
    a[i] = a[i+1]
    a[i+1] = tmp
    return a

if __name__ == '__main__':
    swap()