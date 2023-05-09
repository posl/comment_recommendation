def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for bit in range(2**K):
        dish = [0] * N
        for i in range(K):
            dish[CD[i][(bit>>i)&1] - 1] += 1
        cnt = 0
        for i in range(M):
            if dish[AB[i][0] - 1] > 0 and dish[AB[i][1] - 1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()