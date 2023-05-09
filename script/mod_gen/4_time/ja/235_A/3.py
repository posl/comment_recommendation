def problem235_a():
    a = list(map(int, input()))
    print(a[0] + a[1] + a[2] + a[1] + a[2] + a[0] + a[2] + a[0] + a[1])

if __name__ == '__main__':
    problem235_a()