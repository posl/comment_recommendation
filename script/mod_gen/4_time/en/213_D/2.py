def main():
    N = int(input())
    path = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        path[a-1].append(b-1)
        path[b-1].append(a-1)
    for i in range(N):
        path[i].sort()
    
    ans = [1]
    visited = [False]*N
    visited[0] = True
    now = 0
    while True:
        for i in range(len(path[now])):
            if visited[path[now][i]] == False:
                ans.append(path[now][i]+1)
                visited[path[now][i]] = True
                now = path[now][i]
                break
            if i == len(path[now])-1:
                if now == 0:
                    break
                else:
                    ans.append(now+1)
                    now = ans[-2]-1
        if now == 0:
            break
    print(*ans)

if __name__ == '__main__':
    main()