def problem204_a():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - x - y)

if __name__ == '__main__':
    problem204_a()