Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = (S[i] + A[i]) % M
    ans = 0
    cnt = [0] * M
    for i in range(N + 1):
        ans += cnt[S[i]]
        cnt[S[i]] += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = (B[i] + A[i]) % M

    from collections import defaultdict
    d = defaultdict(int)
    for b in B:
        d[b] += 1

    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2

    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0]
    for i in range(N):
        B.append((B[-1] + A[i]) % M)
    ans = 0
    for x in range(M):
        cnt = 0
        for i in range(N + 1):
            if B[i] == x:
                ans += cnt
                cnt += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
        A[i] %= M
    cnt = [0] * M
    for a in A:
        cnt[a] += 1
    ans = 0
    for c in cnt:
        ans += c * (c-1) // 2
    print(ans)
main()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(1, N+1):
        A[i] = (A[i-1] + A[i]) % M
    A.sort()
    count = 0
    prev = A[0]
    cnt = 1
    for i in range(1, N+1):
        if A[i] == prev:
            cnt += 1
        else:
            count += (cnt * (cnt-1)) // 2
            prev = A[i]
            cnt = 1
    count += (cnt * (cnt-1)) // 2
    print(count)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(1, N + 1):
        A[i] = (A[i] + A[i - 1]) % M
    d = {}
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    ans = 0
    for a in d:
        ans += d[a] * (d[a] - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    summod = [0] * (N + 1)
    for i in range(N):
        summod[i + 1] = (summod[i] + A[i]) % M
    ans = 0
    for i in range(N + 1):
        ans += summod[:i].count(summod[i])
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    #print(A)
    cnt = 0
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += A[j]
            if sum % M == 0:
                cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # A[i]をMで割った余りをA[i]に入れる
    for i in range(N):
        A[i] %= M
    # 余りの累積和をA[i]に入れる
    for i in range(1, N):
        A[i] += A[i-1]
        A[i] %= M
    # 余りの出現回数をカウントする
    counter = [0] * M
    for i in range(N):
        counter[A[i]] += 1
    # 余りの出現回数が2以上のものを組み合わせる
    ans = 0
    for i in range(M):
        ans += counter[i] * (counter[i]-1) // 2
    print(ans)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    # 0-indexed
    a = [0] + a
    # 累積和
    for i in range(1, n + 1):
        a[i] += a[i - 1]
        # 剰余を取る
        a[i] %= m
    # 剰余が同じものがあれば、その間の和はmの倍数
    # 1-indexed
    d = {}
    for i in range(1, n + 1):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    # 2つの選び方
    for k, v in d.items():
        ans += v * (v - 1) // 2
    print(ans)
