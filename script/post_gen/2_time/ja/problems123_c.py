Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print((N-1)//min(A,B,C,D,E)+5)

=======
Suggestion 2

def main():
    N = int(input())
    A, B, C, D, E = map(int, input().split())
    print((N + min(A, B, C, D, E) - 1) // min(A, B, C, D, E) + 4)

=======
Suggestion 3

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min = min(A, B, C, D, E)
    print((N + min - 1) // min + 4)

=======
Suggestion 4

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    min_t = min(A, B, C, D, E)
    print(-(-N // min_t) + 4)

=======
Suggestion 5

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    if N % A == 0:
        ans = 4 + N // A
    else:
        ans = 4 + N // A + 1

    if N % B == 0:
        ans = min(ans, 3 + N // B)
    else:
        ans = min(ans, 3 + N // B + 1)

    if N % C == 0:
        ans = min(ans, 2 + N // C)
    else:
        ans = min(ans, 2 + N // C + 1)

    if N % D == 0:
        ans = min(ans, 1 + N // D)
    else:
        ans = min(ans, 1 + N // D + 1)

    if N % E == 0:
        ans = min(ans, N // E)
    else:
        ans = min(ans, N // E + 1)

    print(ans)

=======
Suggestion 6

def main():
    #入力
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #計算
    #都市 6 に到着するまでに最短で何分かかるか
    min_time = min(A,B,C,D,E)
    #都市 6 に到着するまでにかかる時間を計算
    time = (N + min_time - 1) // min_time
    #出力
    print(time + 4)

=======
Suggestion 7

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #最も移動時間が短い交通機関を探す
    min = A
    if min > B:
        min = B
    if min > C:
        min = C
    if min > D:
        min = D
    if min > E:
        min = E
    print((N + min - 1) // min + 4)
