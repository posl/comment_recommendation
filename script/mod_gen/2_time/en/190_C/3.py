def main():
    N, M = map(int, input().split())
    AB = []
    for _ in range(M):
        AB.append(list(map(int, input().split())))
    K = int(input())
    CD = []
    for _ in range(K):
        CD.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**K):
        dish = [0 for _ in range(N)]
        for j in range(K):
            if i >> j & 1:
                dish[CD[j][0]-1] += 1
            else:
                dish[CD[j][1]-1] += 1
        cnt = 0
        for j in range(M):
            if dish[AB[j][0]-1] > 0 and dish[AB[j][1]-1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()