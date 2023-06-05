def solve(x):
    for a in range(-1000,1000):
        for b in range(-1000,1000):
            if a**5 - b**5 == x:
                return a,b
    return None
x = int(input())
a,b = solve(x)
print(a,b)
