def solve(x):
    for a in range(0, 1001):
        for b in range(0, 1001):
            if a**5 - b**5 == x:
                return a, b
x = int(input())
a, b = solve(x)
print(a, b)

if __name__ == '__main__':
    solve()