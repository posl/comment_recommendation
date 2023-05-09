def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    d = defaultdict(int)
    for x, y in XY:
        d[(x, y)] = 1
    ans = 0
    for x, y in XY:
        if d[(x, y)] == 1:
            ans += 1
            d[(x, y)] = 0
            stack = [(x, y)]
            while stack:
                x, y = stack.pop()
                for dx, dy in [(1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]:
                    if d[(x + dx, y + dy)] == 1:
                        d[(x + dx, y + dy)] = 0
                        stack.append((x + dx, y + dy))
    print(ans)

if __name__ == '__main__':
    main()