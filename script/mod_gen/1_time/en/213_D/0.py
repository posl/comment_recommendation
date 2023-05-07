def main():
    n = int(input())
    roads = {}
    for i in range(n-1):
        a, b = map(int, input().split())
        if a in roads:
            roads[a].append(b)
        else:
            roads[a] = [b]
        if b in roads:
            roads[b].append(a)
        else:
            roads[b] = [a]
    #print(roads)
    visited = [1]
    stack = [1]
    while stack:
        node = stack.pop()
        if node in roads:
            for next in roads[node]:
                if next not in visited:
                    stack.append(next)
                    visited.append(next)
    print(*visited)

if __name__ == '__main__':
    main()