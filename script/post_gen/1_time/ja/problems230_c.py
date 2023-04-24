Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            print("#" if (i+j) % 2 == (A+B) % 2 else ".", end="")
        print()

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (max(1-A, 1-B) <= i-j <= min(N-A, N-B)) or (max(1-A, B-N) <= i+j <= min(N-A, B-1)):
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            if (j - R) % 2 == 0:
                if (i - j + A - B) % 2 == 0 or (i - j + A - B) % 4 == 3:
                    print("#", end="")
                else:
                    print(".", end="")
            else:
                if (i - j + A - B) % 2 == 0 or (i - j + A - B) % 4 == 1:
                    print("#", end="")
                else:
                    print(".", end="")
        print()

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            if (i + j) % 2 == 0:
                if A <= i <= N - B + 1 and A <= j <= N - B + 1:
                    print('#', end='')
                else:
                    print('.', end='')
            else:
                if A <= i <= N - B + 1 and A <= j <= N - B + 1:
                    print('.', end='')
                else:
                    print('#', end='')
        print('')

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            if A <= i <= N - B + 1 and A <= j <= N - B + 1:
                if A + B <= i + j <= N + 1:
                    print("#", end="")
                else:
                    print(".", end="")
            elif 1 <= i <= N - A + 1 and 1 <= j <= N - A + 1:
                if A - B <= i - j <= A - 1:
                    print("#", end="")
                else:
                    print(".", end="")
            else:
                print(".", end="")
        print()

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    #print(N, A, B)
    #print(P, Q, R, S)

    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (max(1-A,1-B) <= i+j-A-B <= min(N-A,N-B)) or (max(1-A,B-N) <= i-j-A+B <= min(N-A,B-1)):
                print('#', end='')
            else:
                print('.', end='')
        print('')
    return

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    # 1 つめの操作で塗られるマスの個数
    c1 = min(N-A, B-1)
    # 2 つめの操作で塗られるマスの個数
    c2 = min(N-A, N-B)
    # 1 つめの操作で塗られるマスの個数
    # 2 つめの操作で塗られるマスの個数
    # のうち、黒く塗られるマスの個数
    c = min(c1, c2)

    for i in range(P, Q+1):
        for j in range(R, S+1):
            if A <= i <= A+c and B-c <= j <= B:
                print("#", end="")
            elif A <= i <= A+c and B <= j <= B+c:
                print("#", end="")
            else:
                print(".", end="")
        print()

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    # 1行目
    for i in range(R, S+1):
        if P <= A + B - i <= Q:
            print("#", end="")
        else:
            print(".", end="")
    print()
    # 2行目以降
    for i in range(P+1, Q+1):
        if i < A + B - S:
            print(".", end="")
        elif i <= A + B - R:
            print("#", end="")
        else:
            print(".", end="")
        if i < A - B + R:
            print("." * (S - R), end="")
        elif i <= A - B + S:
            print("#" * (S - R), end="")
        else:
            print("." * (S - R), end="")
        print()

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    # 1行目の出力
    for i in range(R, S + 1):
        if B - N <= i - B <= B - 1:
            print('#', end='')
        else:
            print('.', end='')
    print()
    # 2行目以降の出力
    for i in range(P + 1, Q + 1):
        # 1列目の出力
        if A - N <= i - A <= A - 1:
            print('#', end='')
        else:
            print('.', end='')
        # 2列目以降の出力
        for j in range(R + 1, S + 1):
            if A - N <= i - A <= A - 1 or B - N <= j - B <= B - 1:
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 10

def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    # (i,j)に置いて、(i,j)を含む対角線の右上にある黒マスの数
    # 1 <= i <= N, 1 <= j <= N
    # 1-indexed
    black = [[0 for j in range(N+1)] for i in range(N+1)]

    # (i,j)に置いて、(i,j)を含む対角線の右上にある白マスの数
    # 1 <= i <= N, 1 <= j <= N
    # 1-indexed
    white = [[0 for j in range(N+1)] for i in range(N+1)]

    # (i,j)に置いて、(i,j)を含む対角線の右上にある白マスの数
    # 1 <= i <= N, 1 <= j <= N
    # 1-indexed
    white = [[0 for j in range(N+1)] for i in range(N+1)]

    # (i,j)に置いて、(i,j)を含む対角線の右上にある白マスの数
    # 1 <= i <= N, 1 <= j <= N
    # 1-indexed
    white = [[0 for j in range(N+1)] for i in range(N+1)]

    # (i,j)に置いて、(i,j)を含む対角線の右上にある白マスの数
    # 1 <= i <= N, 1 <= j <= N
    # 1-indexed
    white = [[0 for j in range(N+1)] for i in range(N+1)]

    # (i,j)に置いて、(i,j)を含む対角線の右上にある白マスの数
    # 1 <= i <= N, 1 <= j <= N
    # 1
