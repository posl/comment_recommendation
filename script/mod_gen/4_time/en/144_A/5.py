def problem():
    a, b = map(int, input().split())
    if 1 <= a <= 20 and 1 <= b <= 20:
        print(a * b if a * b <= 20 else -1)
    else:
        pass

if __name__ == '__main__':
    problem()