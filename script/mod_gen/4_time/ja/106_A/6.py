def problems106_a():
    a, b = map(int, input().split())
    print(a*b - (a+b-1))

if __name__ == '__main__':
    problems106_a()