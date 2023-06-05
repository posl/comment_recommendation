def problem229_b():
    A, B = map(int, input().split())
    if A + B >= 10**9:
        print("Hard")
    else:
        print("Easy")

if __name__ == '__main__':
    problem229_b()