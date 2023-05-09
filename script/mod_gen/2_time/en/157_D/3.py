def main():
    #input
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    #solve
    ans = [0]*N
    for i in range(M):
        ans[AB[i][0]-1] += 1
        ans[AB[i][1]-1] += 1
    for i in range(K):
        if AB[i][0] in CD[i]:
            ans[AB[i][0]-1] -= 1
        if AB[i][1] in CD[i]:
            ans[AB[i][1]-1] -= 1
    #output
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()