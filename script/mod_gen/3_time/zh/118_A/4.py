def problems118_a():
    A, B = map(int, input().split())
    if B % A == 0:
        print(A + B)
    else:
        print(B - A)

if __name__ == '__main__':
    problems118_a()