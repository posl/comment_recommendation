def swap(a, p, q, r, s):
    # 交换p到q和r到s的序列
    b = a[:]
    for i in range(q-p+1):
        b[p+i-1] = a[r+i-1]
    for i in range(s-r+1):
        b[r+i-1] = a[q+i-1]
    return b

if __name__ == '__main__':
    swap()