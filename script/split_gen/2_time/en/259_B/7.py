def main():
    # input
    a, b, d = map(int, input().split())
    # compute
    a, b = a * cos(d) - b * sin(d), a * sin(d) + b * cos(d)
    # output
    print(a, b)
