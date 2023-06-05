def problems157_a():
    n = int(input())
    if n % 2 == 0:
        print(int(n / 2))
    else:
        print(int(n / 2 + 1))
    return

if __name__ == '__main__':
    problems157_a()