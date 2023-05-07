def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    G = {}
    for x, y in XY:
        if (x, y) in G:
            continue
        G[(x, y)] = set()
        for dx, dy in [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]:
            if (x + dx, y + dy) in G:
                G[(x, y)].add((x + dx, y + dy))
                G[(x + dx, y + dy)].add((x, y))
    ans = 0
    while G:
        x, y = list(G.keys())[0]
        q = [(x, y)]
        while q:
            x, y = q.pop()
            if (x, y) in G:
                q += list(G[(x, y)])
                del G[(x, y)]
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()