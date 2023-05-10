def solve():
    a, b, h, m = map(int, input().split())
    import math
    rad = abs(math.radians((h + m/60)*30 - m*6))
    print((a**2 + b**2 - 2*a*b*math.cos(rad))**0.5)
solve()

if __name__ == '__main__':
    solve()