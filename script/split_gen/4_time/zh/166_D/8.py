def solve(x):
    for a in range(-118, 120):
        for b in range(-119, 119):
            if a ** 5 - b ** 5 == x:
                return a, b
x = int(input())
a, b = solve(x)
print(a, b)
