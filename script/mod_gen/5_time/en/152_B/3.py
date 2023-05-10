def problems152_b():
    a, b = map(int, input().split())
    if a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)

if __name__ == '__main__':
    problems152_b()