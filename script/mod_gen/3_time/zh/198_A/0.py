def problem198_a():
    n = int(input())
    if n < 3:
        print(0)
    else:
        print(int((n-1)*(n-2)/2))

if __name__ == '__main__':
    problem198_a()