def solve():
    from collections import deque
    import sys
    input = sys.stdin.readline
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    for dr in range(-4, 5):
        for dc in range(-4, 5):
            if abs(dr) + abs(dc) > 3:
                continue
            if r1 + dr + c1 + dc == r2 + c2 or r1 + dr - c1 - dc == r2 + c2 or r1 - dr + c1 - dc == r2 + c2 or r1 - dr - c1 + dc == r2 + c2:
                print(2)
                return
    print(3)

if __name__ == '__main__':
    solve()