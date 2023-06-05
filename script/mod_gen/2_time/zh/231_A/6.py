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
    i = 0
    j = 0
    now = 0
    while i < N:
        if L[i] <= R[j]:
            now += 1
            i += 1
        else:
            now -= 1
            j += 1
        ans = max(ans, now)
    print(ans)

if __name__ == '__main__':
    main()