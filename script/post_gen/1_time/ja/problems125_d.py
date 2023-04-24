Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    B[0] = A[0]
    for i in range(1, N):
        B[i] = B[i - 1] + A[i]
    B.sort()
    ans = 0
    for i in range(N):
        ans += abs(B[i])
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        if i % 2 == 0:
            B.append(A[i])
        else:
            B.append(A[i] * -1)
    print(sum(B))

main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*N
    B[0] = A[0]
    for i in range(1,N):
        B[i] = B[i-1] + A[i]
    A.sort()
    A = A[::-1]
    ans = 0
    for i in range(N-1):
        ans += A[i]
    ans += B[N-1]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += abs(A[i])
    for i in range(N-1):
        ans += abs(A[i]-A[i+1])
    for i in range(N):
        if i == 0:
            ans -= abs(A[i])
            ans -= abs(A[i+1])
            ans += abs(A[i+1]-A[i])
        elif i == N-1:
            ans -= abs(A[i])
            ans -= abs(A[i-1])
            ans += abs(A[i]-A[i-1])
        else:
            ans -= abs(A[i])
            ans -= abs(A[i-1])
            ans -= abs(A[i+1])
            ans += abs(A[i+1]-A[i-1])
        print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = a[i] + b[i - 1]
    ans = 0
    for i in range(1, n + 1):
        if b[i] > 0:
            ans += b[i]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += abs(a[i])
    ans += abs(a[0])
    ans += abs(a[-1])
    for i in range(n - 1):
        ans -= max(abs(a[i] - a[i + 1]), abs(a[i]) + abs(a[i + 1]))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = sum(A)
    for i in range(1, N-1):
        if A[i-1] < 0 and A[i] < 0 and A[i+1] < 0:
            ans -= min(A[i-1], A[i], A[i+1])
        elif A[i-1] > 0 and A[i] > 0 and A[i+1] > 0:
            ans -= min(A[i-1], A[i], A[i+1])
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 1. B_1 + B_2 + ... + B_N の最大値を求めてください。
    # 2. B_1 + B_2 + ... + B_N の最小値を求めてください。

    # 1. B_1 + B_2 + ... + B_N の最大値を求めてください。
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[i] = A[i]
        else:
            B[i] = -A[i]
    print(sum(B))

    # 2. B_1 + B_2 + ... + B_N の最小値を求めてください。
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[i] = -A[i]
        else:
            B[i] = A[i]
    print(sum(B))

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    #処理
    if N%2 == 0:
        for i in range(N):
            if i%2 == 0:
                A[i] = abs(A[i])
            else:
                A[i] = -abs(A[i])
    else:
        for i in range(N):
            if i%2 == 0:
                A[i] = -abs(A[i])
            else:
                A[i] = abs(A[i])
    print(sum(A))

=======
Suggestion 10

def main():
    N = int(input())
    A = [int(i) for i in input().split()]

    # 全ての要素の絶対値の和を求める
    abs_sum = sum([abs(i) for i in A])

    # すべての要素が負の場合、最大値は abs_sum となる
    if all([i < 0 for i in A]):
        print(abs_sum)
        return

    # すべての要素が正の場合、最大値は abs_sum - 2 * min(A) となる
    if all([i > 0 for i in A]):
        print(abs_sum - 2 * min(A))
        return

    # 要素に正負が混在している場合、最大値は abs_sum - 2 * min(abs(A)) となる
    print(abs_sum - 2 * min([abs(i) for i in A]))
