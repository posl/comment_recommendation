def solve():
    n = int(input())
    ladders = []
    for _ in range(n):
        a, b = map(int, input().split())
        ladders.append((a, b))
    ladders.sort(key=lambda x: x[1])
    current = 1
    for a, b in ladders:
        if a <= current <= b:
            current = b
    print(current)
solve()
