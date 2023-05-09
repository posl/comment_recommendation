def solve():
    k = int(input())
    n = 1
    while n * (n + 1) // 2 < k:
        n += 1
    if n * (n + 1) // 2 == k:
        print(n)
    else:
        print(n + 1)
