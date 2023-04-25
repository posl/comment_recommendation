Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    mi

=======
Suggestion 2

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    mi

=======
Suggestion 3

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    print(h.index(min(h, key=lambda x: abs(a - (t - x * 0.006)))))

=======
Suggestion 4

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    H = [T - h * 0.006 for h in H]
    min_diff = 100
    for i, h in enumerate(H):
        if abs(A - h) < min_diff:
            min_diff = abs(A - h)
            ans = i + 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    avg = [T - h * 0.006 for h in H]
    diff = [abs(a - av) for a, av in zip([A] * N, avg)]
    print(diff.index(min(diff)) + 1)

=======
Suggestion 6

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min_diff = 10**9
    for i in range(N):
        temp = T - H[i] * 0.006
        diff = abs(temp - A)
        if diff < min_diff:
            min_diff = diff
            ans = i + 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 10**9
    ans_index = 0
    for i in range(n):
        if abs(t-h[i]*0.006-a) < ans:
            ans = abs(t-h[i]*0.006-a)
            ans_index = i+1
    print(ans_index)

=======
Suggestion 8

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min = 10**10
    for i in range(n):
        if abs(t-h[i]*0.006-a) < min:
            ans = i+1
            min = abs(t-h[i]*0.006-a)
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min = 100000000000000
    for i in range(n):
        if min > abs(t - h[i] * 0.006 - a):
            min = abs(t - h[i] * 0.006 - a)
            ans = i + 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    # A - T + H[i] * 0.006
    # abs(A - T + H[i] * 0.006)が最小のものを求める
    # abs(A - T + H[i] * 0.006)の最小値を求める
    # abs(A - T + H[i] * 0.006)の最小値と等しいもののインデックスを求める
    # インデックスを出力する

    # 1. abs(A - T + H[i] * 0.006)を求める
    # 2. abs(A - T + H[i] * 0.006)の最小値を求める
    # 3. abs(A - T + H[i] * 0.006)の最小値と等しいもののインデックスを求める
    # 4. インデックスを出力する

    # 1. abs(A - T + H[i] * 0.006)を求める
    # 2. abs(A - T + H[i] * 0.006)の最小値を求める
    # 3. abs(A - T + H[i] * 0.006)の最小値と等しいもののインデックスを求める
    # 4. インデックスを出力する

    # 1. abs(A - T + H[i] * 0.006)を求める
    # 2. abs(A - T + H[i] * 0.006)の最小値を求める
    # 3. abs(A - T + H[i] * 0.006)の最小値と等しいもののインデックスを求める
    # 4. インデックスを出力する

    # 1. abs(A - T + H[i] * 0.006)を求める
