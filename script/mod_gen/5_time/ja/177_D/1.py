def main():
    n,m = map(int,input().split())
    friends = [[] for i in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        friends[a].append(b)
        friends[b].append(a)
    ans = 0
    visited = [False for i in range(n+1)]
    for i in range(1,n+1):
        if visited[i] == False:
            ans += 1
            visited[i] = True
            queue = [i]
            while queue:
                now = queue.pop(0)
                for j in friends[now]:
                    if visited[j] == False:
                        visited[j] = True
                        queue.append(j)
    print(ans)

if __name__ == '__main__':
    main()