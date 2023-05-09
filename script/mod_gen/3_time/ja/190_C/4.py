def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for i in range(K)]
    ans = 0
    for i in range(2**K):
        dish = [0] * (N+1)
        for j in range(K):
            if ((i >> j) & 1):
                dish[CD[j][0]] += 1
            else:
                dish[CD[j][1]] += 1
        count = 0
        for j in range(M):
            if dish[AB[j][0]] > 0 and dish[AB[j][1]] > 0:
                count += 1
        ans = max(ans, count)
    print(ans)

if __name__ == '__main__':
    main()