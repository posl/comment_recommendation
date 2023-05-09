def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    b = [1]
    c = []
    d = 0
    e = 0
    for i in range(1, n+1):
        b.append(a[b[i-1]])
        if b[i] == b[0]:
            d = i
            e = len(b) - d - 1
            break
    if k <= d:
        print(b[k])
    else:
        print(b[(k - d) % e + d])

if __name__ == '__main__':
    main()