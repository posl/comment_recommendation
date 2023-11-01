def problems253_a():
    a, b, c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
