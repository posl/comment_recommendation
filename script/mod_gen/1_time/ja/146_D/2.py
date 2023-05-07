def main():
    N = int(input())
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    colors = [-1]*N
    colors[0] = 1
    stack = [0]
    while stack:
        node = stack.pop()
        color = 1
        for child in edges[node]:
            if colors[child] == -1:
                while color == colors[node]:
                    color += 1
                colors[child] = color
                stack.append(child)
                color += 1
    print(max(colors))
    for i in range(N-1):
        print(colors[i])

if __name__ == '__main__':
    main()