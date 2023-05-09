def main():
    N, M = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(M):
        l, r = map(int, input().split())
        L[l-1] += 1
        R[r-1] += 1
    ans = 0
    cnt = 0
    for i in range(N):
        cnt += L[i]
        if cnt == i + 1:
            ans += 1
        cnt -= R[i]
    print(ans)

if __name__ == '__main__':
    main()