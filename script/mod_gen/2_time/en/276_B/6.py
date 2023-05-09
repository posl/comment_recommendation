def main():
    #input
    N, M = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(M)]
    #compute
    ans = [[] for _ in range(N)]
    for i in range(M):
        ans[AB[i][0]-1].append(AB[i][1])
        ans[AB[i][1]-1].append(AB[i][0])
    for i in range(N):
        ans[i].sort()
        print(len(ans[i]), *ans[i])

if __name__ == '__main__':
    main()