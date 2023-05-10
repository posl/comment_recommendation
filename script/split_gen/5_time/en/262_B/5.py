def main():
    n, m = map(int, input().split())
    edge = []
    for i in range(m):
        edge.append(list(map(int, input().split())))
    ans = 0
    for i in range(m):
        for j in range(i+1, m):
            if edge[i][0] in edge[j] and edge[i][1] in edge[j]:
                ans += 1
    print(ans)
