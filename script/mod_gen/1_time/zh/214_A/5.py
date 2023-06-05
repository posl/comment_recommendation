def problem214_a():
    n = int(input())
    if n < 126:
        print(4)
    elif n < 212:
        print(6)
    else:
        print(8)

if __name__ == '__main__':
    problem214_a()