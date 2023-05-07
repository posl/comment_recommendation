def main():
    n, m = map(int, input().split())
    if m == 0:
        print(3**n)
        return
    edge = []
    for _ in range(m):
        a, b = map(int, input().split())
        edge.append([a, b])
    ans = 0
    for i in range(3**n):
        color = []
        for j in range(n):
            color.append(i // 3**j % 3)
        ok = True
        for j in range(m):
            if color[edge[j][0] - 1] == color[edge[j][1] - 1]:
                ok = False
        if ok:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()