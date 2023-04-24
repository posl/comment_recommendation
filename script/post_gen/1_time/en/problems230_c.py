Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            if (A <= i <= B) and (A <= j <= B):
                print("#", end="")
            elif (A <= i - j <= B - A) and (A <= i + j - 2 * A <= B):
                print("#", end="")
            else:
                print(".", end="")
        print()

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (A <= i <= A+B-1 and R <= j <= S) or (P <= i <= Q and B <= j <= B+A-1):
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i+j) % 2 == 0:
                if A <= i <= N-B+1 and A <= j <= N-B+1:
                    print('#', end='')
                elif 1 <= i <= N-A+1 and 1 <= j <= N-A+1:
                    print('#', end='')
                else:
                    print('.', end='')
            else:
                if A <= i <= N-B+1 and 1 <= j <= N-A+1:
                    print('#', end='')
                elif 1 <= i <= N-A+1 and A <= j <= N-B+1:
                    print('#', end='')
                else:
                    print('.', end='')
        print()

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            if i - j == A - B or i + j == A + B:
                print("#", end="")
            else:
                print(".", end="")
        print()

=======
Suggestion 5

def main():
    N, A, B = [int(i) for i in input().split()]
    P, Q, R, S = [int(i) for i in input().split()]
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (j-i) % 2 == 0:
                if (A <= i <= N-B+1) and (B <= j <= N-A+1):
                    print('#', end='')
                else:
                    print('.', end='')
            else:
                if (A <= i <= N-B+1) and (B <= j <= N-A+1):
                    print('.', end='')
                else:
                    print('#', end='')
        print()

main()

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    if A > B:
        A = N + 1 - A
        B = N + 1 - B
        P = N + 1 - P
        Q = N + 1 - Q
    if A + B - 1 < P:
        for i in range(Q - P + 1):
            print('.' * (S - R + 1))
        return
    if N - A + 1 < R:
        for i in range(Q - P + 1):
            print('.' * (S - R + 1))
        return
    if A + B - 1 > Q:
        for i in range(Q - P + 1):
            print('#' * (S - R + 1))
        return
    if N - A + 1 > S:
        for i in range(Q - P + 1):
            print('#' * (S - R + 1))
        return
    if A + B - 1 >= P and A + B - 1 <= Q:
        print('.' * (A + B - 1 - P) + '#' * (Q - A - B + 2) + '.' * (S - R + 1))
        P = A + B
    if N - A + 1 >= R and N - A + 1 <= S:
        print('.' * (S - R + 1) + '#' * (N - A + 1 - R + 1) + '.' * (N - A))
        S = N - A
    for i in range(P - A - B + 1, Q - A - B + 1):
        if i < 0:
            print('.' * (S - R + 1))
        elif i == 0:
            print('.' * (S - R + 1))
        elif i == 1:
            print('.' * (S - R + 1))
        else:
            print('.' * (S - R + 1))

=======
Suggestion 7

def solve():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            if (i + j) % 2 == 0:
                if (i - A) * (i - A) + (j - B) * (j - B) <= (N - A) * (N - A) + (N - B) * (N - B):
                    print("#", end="")
                else:
                    print(".", end="")
            else:
                if (i - A) * (i - A) + (j - B) * (j - B) <= (A - 1) * (A - 1) + (B - 1) * (B - 1):
                    print("#", end="")
                else:
                    print(".", end="")
        print()

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    #print(N, A, B)
    #print(P, Q, R, S)

    # 1行目の出力
    for j in range(R, S+1):
        if A <= j <= B:
            print('#', end='')
        else:
            print('.', end='')
    print()

    # 2行目以降の出力
    for i in range(P+1, Q+1):
        #print(i)
        #print(i, i-A, i-B)
        #print(i, i-A, i-B, i-A+1, i-B+1)
        #print(i, i-A, i-B, i-A+1, i-B+1, i-A+2, i-B+2)
        #print(i, i-A, i-B, i-A+1, i-B+1, i-A+2, i-B+2, i-A+3, i-B+3)
        #print(i, i-A, i-B, i-A+1, i-B+1, i-A+2, i-B+2, i-A+3, i-B+3, i-A+4, i-B+4)
        #print(i, i-A, i-B, i-A+1, i-B+1, i-A+2, i-B+2, i-A+3, i-B+3, i-A+4, i-B+4, i-A+5, i-B+5)
        #print(i, i-A, i-B, i-A+1, i-B+1, i-A+2, i-B+2, i-A+3, i-B+3, i-A+4, i-B+4, i-A+5, i-B+5, i-A+6, i-B+6)
        #print(i, i-A, i-B, i-A+1, i-B+1, i-A+2, i-B+2, i-A+3, i-B+3, i-A+4, i-B+4, i-A+5, i-B+5, i-A+6, i-B+6, i-A+7, i-B+7)
        #print

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    def f(x):
        if x <= 0:
            return 0
        y = min(N, x)
        return y * (y + 1) // 2

    def g(x):
        if x <= 0:
            return 0
        y = min(N, x)
        return y * (y + 1) * (2 * y + 1) // 6

    def h(x):
        if x <= 0:
            return 0
        y = min(N, x)
        return y * (y + 1) // 2 * (2 * y + 1) // 3

    def calc(x, y):
        return f(x) * f(y) + g(x) * f(y) + f(x) * g(y) + h(x) * f(y) + f(x) * h(y)

    def solve(x, y):
        return calc(x, y) - calc(x - A, y - B) - calc(x - A, y - B + N) - calc(x - A + N, y - B) - calc(x - A + N, y - B + N)

    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            print('#' if solve(i, j) % 2 else '.', end='')
        print()

=======
Suggestion 10

def main():
    N, A, B = list(map(int, input().split()))
    P, Q, R, S = list(map(int, input().split()))
    for i in range(P, Q + 1):
        row = []
        for j in range(R, S + 1):
            if (i <= A and A <= j) or (i <= N - j + 1 and N - j + 1 <= j):
                row.append('#')
            elif (i <= B and B <= j) or (i <= N - j + 1 and N - j + 1 <= j):
                row.append('#')
            else:
                row.append('.')
        print(''.join(row))

main()

Python 3.7.3 (default, May  3 2019, 17:48:47) [GCC 7.4.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> N, A, B = map(int, input().split())
1000000000000000000 999999999999999999 999999999999999999
>>> P, Q, R, S = map(int, input().split())
999999999999999998 1000000000000000000 999999999999999998 1000000000000000000
>>> np.zeros((Q - P + 1, S - R + 1), dtype=str)
array([['', '', ''],
       ['', '', ''],
       ['', '', '']], dtype='<U1')
>>> np.zeros((Q - P + 1, S - R + 1), dtype=str)
array([['', '', ''],
       ['', '', ''],
       ['', '', '']], dtype='<U1')
>>> np.zeros((Q - P + 1, S - R + 1), dtype=str)
array([['', '', ''],
       ['', '', ''],
       ['', '', '']], dtype='<U1')
>>> np.zeros((Q - P + 1, S - R + 1), dtype=str)
array([['', '', ''],
       ['', '', ''],
       ['', '', '']], dtype='<U1')
>>> np.zeros((Q - P + 1, S - R + 1), dtype=str)
array([['', '', ''],
       ['', '', ''],
       ['', '', '']],
