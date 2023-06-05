def problems246_b():
    a,b = [int(i) for i in input().split()]
    x = a * 1.0 / (a * a + b * b) ** 0.5
    y = b * 1.0 / (a * a + b * b) ** 0.5
    print(x,y)

if __name__ == '__main__':
    problems246_b()