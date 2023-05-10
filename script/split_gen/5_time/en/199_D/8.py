def main():
    # Get input here
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        a, b = map(int, input().split())
        edges.append([a, b])
    # Solve problems here
    ans = 0
    for i in range(2 ** n):
        colors = []
        for j in range(n):
            if (i >> j) & 1:
                colors.append(1)
            else:
                colors.append(0)
        flag = True
        for edge in edges:
            if colors[edge[0] - 1] == colors[edge[1] - 1]:
                flag = False
                break
        if flag:
            ans += 1
    # Print result here
    print(ans)
main()
