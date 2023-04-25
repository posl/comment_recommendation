Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    D = [0] * (N + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i] + B[i]] -= 1
    for i in range(1, N + 1):
        D[i] += D[i - 1]
    for i in range(1, N + 1):
        D[i] = D[i - 1] + (D[i] == i)
    for i in range(N):
        print(D[i + 1] - D[i], end=' ')
    print()

=======
Suggestion 2

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    D = [0] * (N + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i] + B[i]] -= 1
    for i in range(1, N + 1):
        D[i] += D[i - 1]
    D.pop(0)
    print(' '.join(map(str, D)))

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    D = [0 for i in range(N+1)]
    for i in range(N):
        D[A[i]-1] += 1
        D[A[i]+B[i]-1] -= 1
    for i in range(1, N):
        D[i] += D[i-1]
    D.pop()
    D.sort()
    print(*D)

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = [0] * (10**5 + 1)
    for i in range(N):
        C[A[i]] += 1
        C[A[i] + B[i]] -= 1
    for i in range(1, 10**5 + 1):
        C[i] += C[i - 1]
    D = [0] * (N + 1)
    for i in range(1, 10**5 + 1):
        D[C[i]] += 1
    for i in range(1, N + 1):
        D[i] += D[i - 1]
    print(*D[1:])

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = list(map(int, input().split()))
        a.append(a_i)
        b.append(b_i)
    d = [0] * (n + 1)
    for i in range(n):
        d[a[i]] += 1
        d[a[i] + b[i]] -= 1
    for i in range(1, n + 1):
        d[i] += d[i - 1]
    for i in range(1, n + 1):
        print(d.count(i))

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for n in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, A, B)
    D = [0] * (10**5 + 1)
    for n in range(N):
        D[A[n]] += 1
        D[A[n] + B[n]] -= 1
    #print(D)
    for i in range(1, 10**5 + 1):
        D[i] += D[i - 1]
    #print(D)
    E = [0] * (N + 1)
    for i in range(1, 10**5 + 1):
        E[D[i]] += 1
    #print(E)
    for i in range(1, N + 1):
        print(E[i], end=' ')
    print()

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #A[i] + B[i] - 1 = Day
    #A[i] + B[i] - 1 = A[i+1] + B[i+1] - 1
    #B[i] =

=======
Suggestion 8

def main():

    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 1日目から10^9日目までの各日にログインした人数をカウント
    # 1日目から10^9日目までの各日にログインした人数の累積和を取る
    # 1日目から10^9日目までの各日にログインした人数の累積和の差分を取る
    # 1日目から10^9日目までの各日にログインした人数の差分を取る
    # 1日目から10^9日目までの各日にログインした人数の差分の累積和を取る
    # 1日目から10^9日目までの各日にログインした人数の差分の累積和を出力

    # 1日目から10^9日目までの各日にログインした人数をカウント
    # 1日目から10^9日目までの各日にログインした人数の累積和を取る
    # 1日目から10^9日目までの各日にログインした人数の累積和の差分を取る
    # 1日目から10^9日目までの各日にログインした人数の差分を取る
    # 1日目から10^9日目までの各日にログインした人数の差分の累積和を取る
    # 1日目から10^9日目までの各日にログインした人数の差分の累積和を出力

    # 1日目から10^9日目までの各日にログインした人数をカウント
    # 1日目から10

=======
Suggestion 9

def read_int():
    return int(input())
