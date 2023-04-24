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
        D[i] = D[i - 1] + D[i]
    for i in range(1, N + 1):
        print(D[i] - D[i - 1], end = ' ')
    print()

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    D = [0] * (N + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i] + B[i]] -= 1
    for i in range(1, N + 1):
        D[i] += D[i - 1]
    D = D[1:]
    print(' '.join(map(str, D)))

=======
Suggestion 3

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # 1日目から10^9日目までのログイン数をカウントする
    # ログイン数は最大でもN人なので、10^9日目までのログイン数はN+1人までカウントできる
    count = [0] * (N + 1)
    for i in range(N):
        # ログイン期間の最初の日にログイン数を+1する
        count[A[i]] += 1
        # ログイン期間の最後の日の次の日にログイン数を-1する
        count[A[i] + B[i]] -= 1

    # 1日目から10^9日目までのログイン数を累積和で求める
    for i in range(1, N + 1):
        count[i] += count[i - 1]

    # 1日目から10^9日目までのログイン数の個数をカウントする
    # ログイン数は最大でもN人なので、10^9日目までのログイン数はN+1人までカウントできる
    result = [0] * (N + 1)
    for i in range(N + 1):
        result[count[i]] += 1

    # 1日目から10^9日目までのログイン数の個数を累積和で求める
    for i in range(1, N + 1):
        result[i] += result[i - 1]

    # 1日目から10^9日目までのログイン数の個数を出力する
    for i in range(1, N + 1):
        print(result[i], end=' ')

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
    D = [0] * (N + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i] + B[i]] -= 1
    for i in range(N):
        D[i + 1] += D[i]
    D = D[1:]
    D.sort()
    print(*D, sep=" ")

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    # 累積和
    # 1日目から10^9日目までのログイン人数
    c = [0] * (10**9+1)
    for i in range(n):
        c[a[i]] += 1
        c[a[i]+b[i]] -= 1

    for i in range(1, 10**9+1):
        c[i] += c[i-1]

    # 1人からn人までのログイン人数
    d = [0] * (n+1)
    for i in range(1, 10**9+1):
        d[c[i]] += 1

    # 累積和
    for i in range(1, n+1):
        d[i] += d[i-1]

    for i in range(1, n+1):
        print(d[i]-d[i-1])

main()

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    days = [0] * (10 ** 9 + 1)
    for i in range(N):
        days[A[i]] += 1
        days[A[i] + B[i]] -= 1
    for i in range(1, 10 ** 9 + 1):
        days[i] += days[i - 1]
    ans = [0] * (N + 1)
    for i in range(1, 10 ** 9 + 1):
        ans[days[i]] += 1
    print(*ans[1:])

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    D = [0 for i in range(N+1)]
    for i in range(N):
        D[A[i]-1] += 1
        D[A[i]+B[i]-1] -= 1
    for i in range(1,N+1):
        D[i] += D[i-1]
    D.pop()
    D.sort()
    print(*D)

=======
Suggestion 8

def main():
    n = int(input())
    A = [0] * n
    B = [0] * n
    for i in range(n):
        A[i], B[i] = map(int, input().split())
    d = [0] * (10 ** 9 + 1)
    for a, b in zip(A, B):
        d[a - 1] += 1
        d[a + b - 1] -= 1
    for i in range(1, 10 ** 9):
        d[i] += d[i - 1]
    for i in range(1, n + 1):
        print(d.count(i))

=======
Suggestion 9

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])

    D = [0] * (N + 1)
    for i in range(N):
        D[0] += AB[i][0] - 1
        D[1] += 1
        D[AB[i][1]] -= 1

    for i in range(1, N + 1):
        D[i] += D[i - 1]

    print(*D[1:])
