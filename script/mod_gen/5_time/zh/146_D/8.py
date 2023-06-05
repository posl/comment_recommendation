def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        a,b = (int(x) for x in input().split())
        edges.append((a,b))
    edges.sort()
    colors = {}
    for a,b in edges:
        if a not in colors:
            colors[a] = 1
        if b not in colors:
            colors[b] = colors[a] + 1
        else:
            colors[b] = max(colors[b],colors[a]+1)
    print(max(colors.values()))
    for a,b in edges:
        print(colors[b])

if __name__ == '__main__':
    main()