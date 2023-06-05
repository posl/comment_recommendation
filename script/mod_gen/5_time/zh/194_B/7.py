def solve():
    N = int(input())
    AB = [list(map(int,input().split())) for _ in range(N)]
    ans = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                ans = min(ans,AB[i][0]+AB[j][1])
            else:
                ans = min(ans,max(AB[i][0],AB[j][1]))
    print(ans)

if __name__ == '__main__':
    solve()