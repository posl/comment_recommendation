def problem200_a():
    n = int(input())
    if n%100 == 0:
        print(int(n/100))
    else:
        print(int(n/100)+1)

if __name__ == '__main__':
    problem200_a()