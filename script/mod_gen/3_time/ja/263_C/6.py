def solve():
    N,M = map(int,input().split())
    ans = []
    for i in range(1,M+1):
        ans.append([i])
    for i in range(1,N):
        tmp = []
        for j in ans:
            for k in range(j[-1]+1,M+1):
                tmp.append(j+[k])
        ans = tmp
    for i in ans:
        print(*i)

if __name__ == '__main__':
    solve()