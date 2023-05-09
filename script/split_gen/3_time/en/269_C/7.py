def solve():
    N = int(input())
    i = 1
    while i <= N:
        if i & N == i:
            print(i)
        i *= 2
