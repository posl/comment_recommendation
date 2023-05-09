def problems271_c(N, a):
    a = sorted(a)
    print(a)
    for i in range(N-1):
        if a[i+1] > a[i]*2:
            return i+1
    return N

if __name__ == '__main__':
    problems271_c()