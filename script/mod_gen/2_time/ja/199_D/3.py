def main():
    n, m = map(int, input().split())
    if m == 0:
        print(3**n)
        return
    edges = [list(map(int, input().split())) for i in range(m)]
    #print(edges)
    #print(edges[0][0])
    #print(edges[0][1])
    #print(edges[1][0])
    #print(edges[1][1])
    #print(edges[2][0])
    #print(edges[2][1])
    #print(edges[3][0])
    #print(edges[3][1])
    #print(edges[4][0])
    #print(edges[4][1])
    #print(edges[5][0])
    #print(edges[5][1])
    ans = 0
    for i in range(3**n):
        color = [0] * (n + 1)
        for j in range(n):
            color[j + 1] = (i // (3**j)) % 3
        #print(color)
        flag = 1
        for j in range(m):
            if color[edges[j][0]] == color[edges[j][1]]:
                flag = 0
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()