def lcm(a,b):
    import fractions
    return a * b // fractions.gcd(a,b)
a,b = map(int,input().split())
print(lcm(a,b))
