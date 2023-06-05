def main():
    n,m = map(int,input().split())
    graph = [[0] * n for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1
    ans = 0
    for i in range(3**n):
        color = [0] * n
        ok = True
        tmp = i
        for j in range(n):
            color[j] = tmp%3
            tmp //= 3
        for j in range(n):
            for k in range(j+1,n):
                if graph[j][k] == 1 and color[j] == color[k]:
                    ok = False
        if ok:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()