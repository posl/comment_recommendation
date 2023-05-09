def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans = 0
    for i in range(N):
        l = L[i]
        r = l + D - 1
        if r > R[i]:
            continue
        else:
            ans += 1
            L[i] = r + 1
    print(ans)

if __name__ == '__main__':
    main()