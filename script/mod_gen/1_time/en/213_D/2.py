def main():
    n = int(input())
    roads = {}
    for i in range(n-1):
        a,b = map(int, input().split())
        if a in roads:
            roads[a].append(b)
        else:
            roads[a] = [b]
        if b in roads:
            roads[b].append(a)
        else:
            roads[b] = [a]
    for i in roads:
        roads[i].sort()
    stack = [1]
    visited = [1]
    while stack:
        current = stack.pop()
        print(current, end=" ")
        for i in roads[current]:
            if i not in visited:
                stack.append(i)
                visited.append(i)
    print()

if __name__ == '__main__':
    main()