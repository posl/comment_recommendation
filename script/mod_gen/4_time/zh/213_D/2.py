def main():
    n = int(input())
    road = {}
    for i in range(n-1):
        a,b = map(int,input().split())
        if a not in road:
            road[a] = [b]
        else:
            road[a].append(b)
        if b not in road:
            road[b] = [a]
        else:
            road[b].append(a)
    print(road)
    visited = [1]
    queue = [1]
    while queue:
        cur = queue.pop(0)
        if cur in road:
            for i in road[cur]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
    print(visited)
    for i in range(len(visited)):
        if i == 0:
            print(visited[i],end=' ')
        elif i == len(visited)-1:
            print(visited[i])
        else:
            print(visited[i],end=' ')

if __name__ == '__main__':
    main()