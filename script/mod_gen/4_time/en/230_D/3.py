def main():
    N, D = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    l = 0
    r = 0
    ans = 0
    while l < N:
        while r < N and L[r] - L[l] < D:
            r += 1
        l = r
        ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()