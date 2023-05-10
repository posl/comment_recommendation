def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(m)
    b = []
    for i in range(n):
        if a[i+1] - a[i] > 1:
            b.append(a[i+1] - a[i] - 1)
    if len(b) == 0:
        print(0)
        return
    else:
        k = min(b)
    c = 0
    for i in range(n):
        c += (a[i] + k - 1)//k
    print(c)
main()

if __name__ == '__main__':
    main()