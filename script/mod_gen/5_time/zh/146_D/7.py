def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        a, b = map(int, input().split())
        edges.append([a, b])
    edges.sort()
    color = [0] * (N+1)
    for i in range(N-1):
        a, b = edges[i][0], edges[i][1]
        if color[a] == 0 and color[b] == 0:
            color[a] = 1
            color[b] = 2
        elif color[a] == 0:
            if color[b] == 1:
                color[a] = 2
            else:
                color[a] = 1
        elif color[b] == 0:
            if color[a] == 1:
                color[b] = 2
            else:
                color[b] = 1
        else:
            pass
    print(max(color))
    for i in range(N-1):
        print(color[edges[i][0]])

if __name__ == '__main__':
    main()