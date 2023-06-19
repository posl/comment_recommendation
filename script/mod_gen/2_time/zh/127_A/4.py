def problem127_a():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6:
        print(int(B/2))
    else:
        print(0)

if __name__ == '__main__':
    problem127_a()