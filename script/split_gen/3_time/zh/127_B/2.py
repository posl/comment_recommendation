def solve(r, D, x_2000):
    for i in range(10):
        x_2000 = r * x_2000 - D
        print(x_2000)
