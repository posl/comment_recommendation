def solve():
    a, b = map(int, input().split())
    print((a * b) // math.gcd(a, b))
