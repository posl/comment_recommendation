def main():
    n = int(input())
    L = []
    R = []
    for i in range(n):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    l = L[0]
    r = R[0]
    for i in range(1, n):
        if l < L[i]:
            l = L[i]
        if r > R[i]:
            r = R[i]
    if l < r:
        print(l, r)
    else:
        print(0)

if __name__ == '__main__':
    main()