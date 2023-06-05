def main():
    N, M = [int(x) for x in input().split()]
    sc = []
    for i in range(M):
        sc.append([int(x) for x in input().split()])
    sc.sort(key=lambda x: x[0])
    if sc[0][0] == 1 and sc[0][1] == 0:
        print(-1)
        return
    num = [0] * N
    for i in range(M):
        num[sc[i][0] - 1] = sc[i][1]
    ans = 0
    for i in range(N):
        ans = ans * 10 + num[i]
    print(ans)

if __name__ == '__main__':
    main()