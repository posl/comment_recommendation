def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        D = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                D[CD[j][1]] += 1
            else:
                D[CD[j][0]] += 1
        cnt = 0
        for j in range(M):
            if D[AB[j][0]] > 0 and D[AB[j][1]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()