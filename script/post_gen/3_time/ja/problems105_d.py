Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = (B[i] + A[i]) % M
    D = {}
    for i in range(N + 1):
        if B[i] in D:
            D[B[i]] += 1
        else:
            D[B[i]] = 1
    ans = 0
    for i in D:
        if D[i] > 1:
            ans += D[i] * (D[i] - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    mod = [0] * M
    mod[0] = 1
    s = 0
    for i in range(N):
        s = (s + A[i]) % M
        ans += mod[s]
        mod[s] += 1
    print(ans)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum = [0] * (n + 1)
    for i in range(n):
        sum[i + 1] = sum[i] + a[i]
    cnt = [0] * m
    for i in range(n + 1):
        cnt[sum[i] % m] += 1
    ans = 0
    for i in range(m):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #A = [4, 1, 5]
    #N = 3
    #M = 2
    #A = [29, 7, 5, 7, 9, 51, 7, 13, 8, 55, 42, 9, 81

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(1, N + 1):
        A[i] += A[i - 1]
        A[i] %= M
    A = sorted(A)
    cnt = 0
    now = 0
    for i in range(1, N + 1):
        if A[i] == A[i - 1]:
            now += 1
        else:
            cnt += now * (now + 1) // 2
            now = 0
    cnt += now * (now + 1) // 2
    print(cnt)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]

    # 累積和を求める
    cumsum = [0]
    for a in A:
        cumsum.append((cumsum[-1] + a) % M)

    # 累積和のリストから、同じ値が何個あるかをカウントする
    # 例えば、[0, 1, 1, 2, 2, 2, 3, 3, 4] なら、
    # 0: 1個、1: 2個、2: 3個、3: 2個、4: 1個
    from collections import Counter
    count = Counter(cumsum)

    # 組み合わせの数を求める
    # 例えば、[0, 1, 1, 2, 2, 2, 3, 3, 4] なら、
    # 0: 1個、1: 2個、2: 3個、3: 2個、4: 1個
    # から 1個、2個、3個の組み合わせの総和を求める
    ans = 0
    for v in count.values():
        ans += v * (v - 1) // 2

    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    # 累積和
    B = [0]
    for i in range(N):
        B.append(B[i] + A[i])
    # print(B)
    # あまりの個数
    C = [0] * M
    for i in range(N + 1):
        C[B[i] % M] += 1
    # print(C)
    # あまりの個数から組み合わせを計算
    for i in range(M):
        ans += C[i] * (C[i] - 1) // 2
    print(ans)

=======
Suggestion 8

def  main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    mod_A = [0] * (N + 1)
    for i in range(N):
        mod_A[i + 1] = (mod_A[i] + A[i]) % M
    mod_A.sort()
    ans = 0
    cnt = 1
    for i in range(N):
        if mod_A[i] == mod_A[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Aの累積和を取る
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = sum_A[i] + A[i]
    # Mで割った余りを取る
    for i in range(N + 1):
        sum_A[i] %= M
    # Mで割った余りが同じ要素同士の組み合わせを数える
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N + 1):
        d[sum_A[i]] += 1
    # 2つ選ぶ組み合わせを数える
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 余りの個数をカウントするリスト
    remainder = [0] * M
    # 累積和
    cumsum = 0
    for i in range(N):
        cumsum += A[i]
        # 余りを求める
        remainder[cumsum % M] += 1
    # 組み合わせを求める
    ans = 0
    for i in range(M):
        # 余りが i であるものの組み合わせを求める
        ans += remainder[i] * (remainder[i] - 1) // 2
    print(ans)
