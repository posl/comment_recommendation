def problem155a():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print("Yes")
    elif a == c and b != c:
        print("Yes")
    elif b == c and a != b:
        prin

if __name__ == '__main__':
    problem155a()