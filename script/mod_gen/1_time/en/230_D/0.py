def main():
    N, D = map(int, input().split())
    L, R = [], []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans = 0
    for i in range(N):
        ans += max(0, L[i] - R[i - 1] - D)
        ans += max(0, R[i] - L[i + 1] - D)
    print(ans)
main()

if __name__ == '__main__':
    main()