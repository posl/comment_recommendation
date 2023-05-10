def min_time():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    return min(max(min(a), max(b)), max(min(b), max(a)))
print(min_time())
