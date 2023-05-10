def problem144_a():
    a, b = map(int, input().split())
    if a in range(1,10) and b in range(1,10):
        print(a*b)
    else:
        print(-1)

if __name__ == '__main__':
    problem144_a()