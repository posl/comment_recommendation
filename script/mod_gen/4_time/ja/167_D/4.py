def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [-1]*n
    b[0] = 0
    c = [0]
    d = [0]
    e = 0
    while True:
        e = a[e]-1
        c.append(e)
        if b[e] != -1:
            break
        b[e] = len(c)-1
    f = b[e]
    g = len(c)-1-f
    if k < f:
        print(c[k]+1)
    else:
        k -= f
        k %= g
        print(c[f+k]+1)

if __name__ == '__main__':
    main()