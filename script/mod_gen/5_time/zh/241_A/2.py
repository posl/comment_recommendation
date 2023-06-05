def problem241_a():
    a = input().split()
    for i in range(3):
        a = a[int(a[0])]
    print(a)

if __name__ == '__main__':
    problem241_a()