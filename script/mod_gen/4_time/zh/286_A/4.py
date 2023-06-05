def main():
    n,p,q,r,s = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        if i >= p-1 and i <= q-1:
            b.append(a[i+r-q])
        elif i >= r-1 and i <= s-1:
            b.append(a[i-q+p])
        else:
            b.append(a[i])
    print(' '.join(map(str, b)))

if __name__ == '__main__':
    main()