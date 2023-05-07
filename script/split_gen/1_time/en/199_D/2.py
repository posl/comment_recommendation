def main():
    n, m = map(int, input().split())
    if m == 0:
        print(3**n)
        return
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))
    #print(edges)
    ans = 0
    for i in range(3**n):
        colors = [0]*n
        for j in range(n):
            colors[j] = i // (3**j) % 3
        #print(colors)
        flag = True
        for edge in edges:
            if colors[edge[0]-1] == colors[edge[1]-1]:
                flag = False
        if flag:
            ans += 1
    print(ans)
