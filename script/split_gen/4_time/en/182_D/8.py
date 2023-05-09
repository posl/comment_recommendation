def solve():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    max_pos = 0
    for i in range(n):
        total += a[i]
        if total > max_pos:
            max_pos = total
    return max_pos
print(solve())
