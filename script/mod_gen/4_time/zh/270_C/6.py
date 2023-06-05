def main():
    n,x,y = map(int,input().split())
    n -= 1
    x -= 1
    y -= 1
    edges = [list(map(int,input().split())) for _ in range(n)]
    edges.sort(key=lambda x:x[0])
    edges.sort(key=lambda x:x[1])
    print(edges)
    print(x,y)
    for i in range(n):
        if edges[i][0] == x:
            print(edges[i][0],edges[i][1])
            x = edges[i][1]
        elif edges[i][1] == x:
            print(edges[i][0],edges[i][1])
            x = edges[i][0]
        if edges[i][0] == y:
            print(edges[i][0],edges[i][1])
            y = edges[i][1]
        elif edges[i][1] == y:
            print(edges[i][0],edges[i][1])
            y = edges[i][0]

if __name__ == '__main__':
    main()