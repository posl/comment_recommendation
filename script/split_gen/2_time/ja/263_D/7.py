def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    # 0 から N までの総和を求める
    s = [0] * (N + 1)
    for i in range(1, N + 1):
        s[i] = s[i - 1] + A[i - 1]
    # 0 から i までの総和を求める
    # 0 から i までの総和の最小値を求める
    # 0 から i までの総和の最小値の最大値を求める
    # 0 から i までの総和の最小値の最大値と s[i] の差が最大となる i を求める
    # その差が答え
    ans = -float('inf')
    for i in range(N + 1):
        ans = max(ans, s[i] - min(s[:i + 1]))
    print(ans + L + R)
