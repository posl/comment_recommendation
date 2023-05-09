def swap(a, b, c, d):
    #a = list, b = p, c = q, d = r, e = s
    e = d
    temp = a[b-1:c]
    a[b-1:c] = a[d-1:e]
    a[d-1:e] = temp
    return a

if __name__ == '__main__':
    swap()