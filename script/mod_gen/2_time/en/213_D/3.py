def main():
    n = int(input())
    road = [[] for _ in range(n)]
    for i in range(n-1):
        a,b = map(int,input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)
    #print(road)
    visited = [0]*n
    visited[0] = 1
    stack = [0]
    res = []
    while stack:
        v = stack.pop()
        res.append(v+1)
        for i in road[v]:
            if visited[i] == 0:
                visited[i] = 1
                stack.append(i)
                stack.append(v)
    print(*res)

if __name__ == '__main__':
    main()