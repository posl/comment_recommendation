def candy(N,K,c):
    c.sort()
    #print(c)
    #print(c[K-1])
    #print(c[N-1])
    #print(c[N-K])
    if c[K-1] == c[N-1]:
        return 1
    elif c[K-1] == c[N-K]:
        return c[N-1] - c[K-1] + 1
    else:
        return c[N-1] - c[K-1] + 2

if __name__ == '__main__':
    candy()