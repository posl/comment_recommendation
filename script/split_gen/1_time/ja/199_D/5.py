def main():
    n, m = map(int, input().split())
    edge = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        a,b = map(int, input().split())
        edge[a-1][b-1] = 1
        edge[b-1][a-1] = 1
    #print(edge)
    color = [0 for i in range(n)]
    for i in range(n):
        color[i] = 3
    #print(color)
    ans = 0
    for i in range(3**n):
        tmp = i
        for j in range(n):
            color[j] = tmp % 3
            tmp //= 3
        #print(color)
        flag = 0
        for j in range(n):
            for k in range(j + 1, n):
                if edge[j][k] == 1 and color[j] == color[k]:
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 0:
            ans += 1
    print(ans)
