Synthesizing 9/10 solutions

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = (B[i] + A[i]) % M
    ans = 0
    for i in range(N):
        ans += B[i + 1:].count(B[i])
    print(ans)

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = sum_A[i] + A[i]
    sum_A = list(map(lambda x: x % M, sum_A))
    sum_A_dict = {}
    for i in range(N + 1):
        if sum_A[i] in sum_A_dict:
            sum_A_dict[sum_A[i]] += 1
        else:
            sum_A_dict[sum_A[i]] = 1
    ans = 0
    for i in range(M):
        if i in sum_A_dict:
            ans += sum_A_dict[i] * (sum_A_dict[i] - 1) // 2
    print(ans)

=======

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    mod = [0] * m
    mod[0] = 1
    s = 0
    for i in range(n):
        s = (s + a[i]) % m
        ans += mod[s]
        mod[s] += 1
    print(ans)

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    cumsum = [0] * (N + 1)
    for i in range(N):
        cumsum[i + 1] = cumsum[i] + A[i]
    # モジュロの性質より、
    # cumsum[i] % M == cumsum[j] % M となるとき、
    # cumsum[i + 1] % M == cumsum[j + 1] % M となる。
    # つまり、cumsum[i + 1] % M をキーとして、
    # その値として、そのキーを持つ累積和の個数を保存する。
    # 例えば、
    # cumsum[0] % M == 0
    # cumsum[2] % M == 0
    # cumsum[3] % M == 0
    # となった場合、
    # 0, 2, 3 をキーとして、
    # その値として、そのキーを持つ累積和の個数を保存する。
    # すなわち、
    # {0: 1, 2: 1, 3: 1}
    # となる。
    # この場合、
    # cumsum[0] % M == cumsum[3] % M となる。
    # つまり、
    # cumsum[0 + 1] % M == cumsum[3 + 1] % M となる。
    # つまり、
    # cumsum[1] % M == cumsum[4] % M となる。
    # すなわち、
    # 0, 2, 3, 4 をキーとして、
    # その値として、そのキーを持つ累積和の個数を保存する。
    # すなわち、
    # {0: 2, 2:

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 累積和
    sum = [0]
    for i in range(N):
        sum.append(sum[i] + A[i])

    # 各累積和を M で割った余りを求める
    mod = []
    for i in range(N+1):
        mod.append(sum[i] % M)

    # 余りが同じものの組み合わせを求める
    ans = 0
    d = {}
    for i in range(N+1):
        if mod[i] in d:
            d[mod[i]] += 1
        else:
            d[mod[i]] = 1

    for i in range(M):
        if i in d:
            ans += d[i] * (d[i] - 1) // 2

    print(ans)

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    # 累積和を計算
    s = [0] * (N+1)
    for i in range(N):
        s[i+1] = (s[i] + A[i]) % M
    # 累積和の値の出現回数を数える
    cnt = [0] * M
    for i in range(N+1):
        cnt[s[i]] += 1
    # 組 (l, r) に対する和 A_l + A_{l+1} + ... + A_r が M の倍数であるとき、
    # 累積和 s[r+1] と s[l] の差が M の倍数であることを利用する
    for i in range(M):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # A = [4,1,5] # 3
    # A = [29,7,5,7,9,51,7,13,8

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 余りの数を格納する配列
    R = [0] * M
    # 余りの数を数える
    for a in A:
        R[a % M] += 1
    # 余りの数を数える
    ans = R[0] * (R[0] - 1) // 2
    for i in range(1, M // 2 + 1):
        if i != M - i:
            ans += R[i] * R[M - i]
    print(ans)

=======

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    # ある要素までの和を計算する
    for i in range(1, N):
        A[i] += A[i - 1]
    # ある要素までの和をMで割った余りを計算する
    for i in range(N):
        A[i] %= M
    # 余りの数をカウントする
    cnt = [0] * M
    for a in A:
        cnt[a] += 1
    # 余りが同じものを2つ選ぶ組み合わせを求める
    for c in cnt:
        ans += c * (c - 1) // 2
    # 余りが0のものを選ぶ組み合わせを加える
    ans += cnt[0]
    print(ans)
