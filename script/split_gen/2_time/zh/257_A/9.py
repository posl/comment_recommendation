def problems257_a():
    n, x = map(int, raw_input().split())
    print chr(64 + (x-1)/n)
