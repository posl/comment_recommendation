def problems257_a():
    n, x = map(int, input().split())
    print(chr(x % 26 + 64))
