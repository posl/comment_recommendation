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
        ans += 1
        if i == 0:
            ans += 1
        if i == N-1:
            ans += 1
        ans += (L[i] - R[i-1] - 1) // D
    print(ans)

if __name__ == '__main__':
    main()