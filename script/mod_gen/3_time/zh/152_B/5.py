def problem152_b():
    a, b = map(int, input().split())
    if a == b:
        print(str(a) * a)
    elif a < b:
        print(str(a) * b)
    else:
        print(str(b) * a)

if __name__ == '__main__':
    problem152_b()