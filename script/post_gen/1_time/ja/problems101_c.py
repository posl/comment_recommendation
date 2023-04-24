Synthesizing 7/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print((N - 1 + K - 2) // (K - 1))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - K + 1):
        if A[i] != i + 1:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - K + 1):
        ans += 1
        for j in range(K):
            A[i + j] = 0
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 1, 2, ..., N を並び替えたものになっているので、
    # 1, 2, ..., N の時の値を求める
    A = [a - 1 for a in A]

    # 1, 2, ..., N の時の値が、
    # 0, 1, ..., N-1 となっているので、
    # 0, 1, ..., N-1 の時の値を求める
    A = [a - i for a, i in zip(A, range(N))]

    # 0, 1, ..., N-1 の時の値が、
    # 0, 1, ..., N-1 となっているので、
    # 0, 1, ..., N-1 の時に何回操作するかを求める
    A = [a // K for a in A]

    # 0, 1, ..., N-1 の時に何回操作するかが、
    # 0, 1, ..., N-1 となっているので、
    # 0, 1, ..., N-1 の時に何回操作するかの最大値を求める
    max_cnt = max(A)

    # 0, 1, ..., N-1 の時に何回操作するかの最大値が、
    # 0, 1, ..., N-1 となっているので、
    # 0, 1, ..., N-1 の時に何回操作するかの最大値を求める
    print(max_cnt + 1)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i < K:
            continue
        ans += A[i]
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    ans = 0
    while True:
        if a == list(range(n)):
            break
        for i in range(n - k + 1):
            if a[i] == a[i + k - 1]:
                continue
            min_a = min(a[i:i + k])
            for j in range(i, i + k):
                a[j] = min_a
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A

    # シミュレーション
    # 1回の操作で、連続するK個の要素の最小値を求める
    # これを全ての要素が同じ値になるまで繰り返す
    # ただし、連続するK個の要素の最小値がK個以上ある場合は、
    # 最小値のうちK個を選んで、それ以外を最小値にする
    # この操作は、最小値のうちK個を選んで、それ以外を最小値にする
    # という操作を繰り返すことと等しい
    # 操作回数を数える
    cnt = 0
    while True:
        # 最小値の個数をカウント
        min_cnt = 0
        for i in range(1, N+1):
            if A[i] == min(A):
                min_cnt += 1
        if min_cnt == N:
            break
        # 最小値の個数がK個以上ある場合
        if min_cnt >= K:
            # 最小値のうちK個を選んで、それ以外を最小値にする
            for i in range(1, N+1):
                if A[i] == min(A):
                    A[i] = min(A)
                else:
                    A[i] = min(A)+1
            cnt += 1
        # 最小値の個数がK個未満の場合
        else:
            # 最小値のうちK個を選んで、それ以外を最小値にする
            for i in range(1, N+1):
                if A[i] == min(A):
                    A[i] = min(A)
                else:
                    A[i] = min(A)+1
