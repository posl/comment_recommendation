def print_x(r, D, x):
    for i in range(10):
        x = r * x - D
        print(x)
r, D, x = map(int, input().split())
print_x(r, D, x)
