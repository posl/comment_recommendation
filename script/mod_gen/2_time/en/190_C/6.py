def main():
    N,M = map(int,input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int,input().split())))
    K = int(input())
    CD = []
    for j in range(K):
        CD.append(list(map(int,input().split())))
    ans = 0
    for i in range(2**K):
        dish = [0] * (N+1)
        for j in range(K):
            if (i >> j) & 1:
                dish[CD[j][1]] += 1
            else:
                dish[CD[j][0]] += 1
        count = 0
        for k in range(M):
            if dish[AB[k][0]] > 0 and dish[AB[k][1]] > 0:
                count += 1
        ans = max(ans,count)
    print(ans)

if __name__ == '__main__':
    main()