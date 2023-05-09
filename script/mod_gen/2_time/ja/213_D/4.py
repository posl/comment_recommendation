def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    ans = [1]
    visited = [False]*N
    visited[0] = True
    while True:
        flag = False
        for i in graph[ans[-1]-1]:
            if not visited[i]:
                ans.append(i+1)
                visited[i] = True
                flag = True
                break
        if not flag:
            if ans[-1] == 1:
                break
            else:
                ans.append(ans[-2])
    print(*ans)

if __name__ == '__main__':
    main()