def check(x, y, h):
    for cx in range(101):
        for cy in range(101):
            H = h + abs(x - cx) + abs(y - cy)
            if all([max(H - abs(x - cx) - abs(y - cy), 0) == h for x, y, h in lst]):
                return cx, cy, H
    return -1, -1, -1
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
for x, y, h in lst:
    if h > 0:
        cx, cy, H = x, y, h
        break
cx, cy, H = check(cx, cy, H)
print(cx, cy, H)

if __name__ == '__main__':
    check()