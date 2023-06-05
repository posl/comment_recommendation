def problems246_b():
    a, b = map(int, input().split())
    print(b / (a ** 2 + b ** 2) ** 0.5, a / (a ** 2 + b ** 2) ** 0.5)

if __name__ == '__main__':
    problems246_b()