def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0]
    for i in range(N):
        B.append((B[-1] + A[i]) % M)
    ans = 0
    for x in range(M):
        cnt = 0
        for i in range(N + 1):
            if B[i] == x:
                ans += cnt
                cnt += 1
    print(ans)

if __name__ == '__main__':
    main()