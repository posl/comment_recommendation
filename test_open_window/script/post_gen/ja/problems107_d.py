Synthesizing 9/10 solutions

=======

def median(a):
    n = len(a)
    if n % 2 == 0:
        return (a[n//2-1] + a[n//2]) / 2
    else:
        return a[n//2]

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append((A[i], i))
    B.sort()
    C = [0] * N
    for i in range(N):
        C[B[i][1]] = i
    BIT = [0] * (N + 1)
    def add(x, w):
        while x <= N:
            BIT[x] += w
            x += x & -x
    def sum(x):
        s = 0
        while x > 0:
            s += BIT[x]
            x -= x & -x
        return s
    def median():
        l, r = 0, N + 1
        while r - l > 1:
            m = (l + r) // 2
            if sum(m) < (N + 1) // 2:
                l = m
            else:
                r = m
        return r
    ans = 0
    for i in range(N):
        add(C[i] + 1, 1)
        ans += median()
    print(ans)

main()

=======

def main():
    n = int(input())
    a = list(map(int, input().split()))

    m = [0] * (n * (n + 1) // 2)
    l = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            m[l] = a[i:j]
            l += 1

    ans = 0
    for i in range(len(m)):
        m[i].sort()
        ans += m[i][len(m[i]) // 2]

    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [10, 30, 20]
    # N = 3
    # A = [10]
    # N = 1
    # A = [5, 9, 5, 9, 8, 9, 3, 5, 4, 3]
    # N = 10
    # A = [10, 30, 20, 40]
    # N = 4
    # A = [10, 10, 10, 20, 30]
    # N = 5
    # A = [10, 30, 20, 40]
    # N = 4
    # A = [10, 10, 10, 20, 30]
    # N = 5
    # A = [10, 30, 20, 40]
    # N = 4
    # A = [10, 10, 10, 20, 30]
    # N = 5
    # A = [10, 30, 20, 40]
    # N = 4
    # A = [10, 10, 10, 20, 30]
    # N = 5
    # A = [10, 30, 20, 40]
    # N = 4
    # A = [10, 10, 10, 20, 30]
    # N = 5
    # A = [10, 30, 20, 40]
    # N = 4
    # A = [10, 10, 10, 20, 30]
    # N = 5
    # A = [10, 30, 20, 40]
    # N = 4
    # A = [10, 10, 10, 20, 30]
    # N = 5
    # A = [10, 30, 20, 40]
    # N = 4
    # A = [10, 10, 10, 20, 30]
    # N = 5
    # A = [10, 30, 20,

=======

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #各区間の中央値を求める
    B = []
    for i in range(N):
        for j in range(i, N):
            B.append(sorted(A[i:j+1])[len(A[i:j+1])//2])
    #中央値を求める
    print(sorted(B)[len(B)//2])

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = 10**9 + 7

    def f(x):
        return x * (x + 1) // 2 % M

    def g(x):
        return x * (x + 1) * (2 * x + 1) // 6 % M

    ans = 0
    for i in range(N):
        ans += A[i] * (f(i) * (N - i - 1) + f(N - i - 1) * i + g(N - i - 1) + g(i)) % M
    print(ans % M)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 連続部分列の中央値をメモする
    memo = []
    for i in range(N):
        memo.append([A[i]])
        for j in range(i+1, N):
            memo[i].append(A[j])
            if len(memo[i]) % 2 == 0:
                memo[i].sort()
                memo[i].pop(0)

    # 中央値をメモする
    memo2 = []
    for i in range(N):
        for j in range(N-i):
            memo2.append(memo[j][i])

    memo2.sort()
    print(memo2[len(memo2)//2])

=======

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 入力を昇順にソート
    b = sorted(a)

    # 中央値の位置
    mid = n // 2

    # 中央値の位置の値
    mid_v = b[mid]

    # 中央値を超える値の数
    over = [0] * (n + 1)

    # 中央値を超える値の数を計算
    for i in range(mid + 1, n):
        over[i] = over[i - 1] + b[i] - mid_v

    # 中央値を超える値の数を計算
    for i in range(mid - 1, -1, -1):
        over[i] = over[i + 1] + mid_v - b[i]

    # 中央値を超える値の数を計算
    for i in range(n):
        print(over[i] + a[i] - mid_v)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [random.randint(1, 10**9) for _ in range(N)]
    As = sorted(A)
    As = [0] + As + [0]
    M = N * (N + 1) // 2
    B = [0] * M
    idx = 0
    for i in range(N):
        for j in range(i, N):
            B[idx] = As[j + 1]
            idx += 1
    B.sort()
    print(B[M // 2])
