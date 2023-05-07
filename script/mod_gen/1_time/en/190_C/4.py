def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(1 << K):
        dish = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                dish[CD[j][1]] += 1
            else:
                dish[CD[j][0]] += 1
        cnt = 0
        for a, b in AB:
            if dish[a] > 0 and dish[b] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()