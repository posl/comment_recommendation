def solution1():
    N, A, B = map(int, input().split())
    if A + B == 0:
        print(0)
        return
    if N == 1:
        if A > 0:
            print(1)
        else:
            print(0)
        return
    if A == 0:
        print(0)
        return
    if B == 0:
        print(1)
        return
    if N <= A:
        print(N)
        return
    if N == A + 1:
        print(A)
        return
    if N == A + 2:
        print(A + 1)
        return
    if A <= N <= A + B:
        print(A)
        return
    if N == A + B + 1:
        print(A + 1)
        return
    if N == A + B + 2:
        print(A + 2)
        return
    if A + B + 3 <= N <= 2 * A + B + 2:
        print(N - A - 1)
        return
    if N == 2 * A + B + 3:
        print(A + 1)
        return
    if N == 2 * A + B + 4:
        print(A + 2)
        return
    if 2 * A + B + 5 <= N <= 2 * A + 2 * B + 4:
        print(A + 2)
        return
    if N == 2 * A + 2 * B + 5:
        print(A + 2)
        return
    if N == 2 * A + 2 * B + 6:
        print(A + 3)
        return
    if 2 * A + 2 * B + 7 <= N <= 3 * A + 2 * B + 6:
        print(A + 3)
        return
    if N == 3 * A + 2 * B + 7:
        print(A + 3)
        return
    if N == 3 * A + 2 * B + 8:
        print(A + 4)
        return
    if 3 * A + 2 * B + 9 <= N <= 3 * A + 3 * B + 8:
        print(A

if __name__ == '__main__':
    solution1()