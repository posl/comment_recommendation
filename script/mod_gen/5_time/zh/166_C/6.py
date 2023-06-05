def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    a = []
    b = []
    for i in range(m):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        b.append(tmp[1])
    # print(n, m)
    # print(h)
    # print(a)
    # print(b)
    result = [1] * n
    for i in range(m):
        if h[a[i]-1] <= h[b[i]-1]:
            result[a[i]-1] = 0
        if h[b[i]-1] <= h[a[i]-1]:
            result[b[i]-1] = 0
    print(sum(result))

if __name__ == '__main__':
    main()