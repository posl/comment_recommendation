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
        if i == N - 1:
            break
        if L[i + 1] - R[i] > D:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()