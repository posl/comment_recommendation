def solve():
    l = int(input())
    n = l + 1
    m = l * (l + 1) // 2
    print(n, m)
    for i in range(1, l + 1):
        print(i, i + 1, 0)
    for i in range(1, l):
        print(i, i + 1, l - i)
