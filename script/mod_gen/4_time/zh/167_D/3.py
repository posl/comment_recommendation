def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [1]
    for i in range(1, n+1):
        b.append(a[b[i-1]-1])
    c = [1]
    for i in range(1, n+1):
        c.append(b[i])
        if c.count(c[i]) == 2:
            break
    if k < i:
        print(c[k+1])
    else:
        print(c[(k-i)%(i+1)+i+1])

if __name__ == '__main__':
    main()