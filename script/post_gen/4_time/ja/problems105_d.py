Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    for i in range(n + 1):
        s[i] %= m
    from collections import Counter
    c = Counter(s)
    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 2

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]

    from collections import defaultdict
    d = defaultdict(int)
    for s in S:
        d[s%M] += 1

    ans = 0
    for v in d.values():
        ans += v*(v-1)//2
    print(ans)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 累積和を M で割った余りの個数を数える
    from collections import Counter
    C = Counter([s % M for s in S])
    ans = 0
    # 余りが同じ累積和の組み合わせを数える
    for c in C.values():
        ans += c * (c - 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    for i in range(N):
        A[i+1] += A[i]
    mod = {}
    for i in range(N+1):
        if A[i] % M not in mod:
            mod[A[i] % M] = 0
        mod[A[i] % M] += 1
    ans = 0
    for i in mod:
        ans += mod[i] * (mod[i] - 1) // 2
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和を求める
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 各 S[i] を M で割った余りを求める
    T = [x % M for x in S]
    # T の要素のうち、2つ以上同じものがあるものの数を求める
    from collections import Counter
    C = Counter(T)
    ans = 0
    for c in C.values():
        ans += c * (c - 1) // 2
    print(ans)

=======
Suggestion 6

def solve():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] %= M
    S = [0]
    for i in range(N):
        S.append((S[-1]+A[i])%M)
    from collections import defaultdict
    D = defaultdict(int)
    for s in S:
        D[s] += 1
    ans = 0
    for k,v in D.items():
        ans += v*(v-1)//2
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 累積和を計算
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    # 累積和を M で割った余りごとに個数を数える
    cnt = {}
    for v in s:
        r = v % m
        if r in cnt:
            cnt[r] += 1
        else:
            cnt[r] = 1
    # 余りが同じ個数のペアの数を数える
    ans = 0
    for v in cnt.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a = [i%m for i in a]
    b = [0]
    for i in range(n):
        b.append((b[-1]+a[i])%m)
    from collections import Counter
    c = Counter(b)
    ans = 0
    for i in c:
        ans += c[i]*(c[i]-1)//2
    print(ans)

=======
Suggestion 9

def solution():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    sum_a = [0 for _ in range(n+1)]
    for i in range(n):
        sum_a[i+1] = sum_a[i] + a[i]
    from collections import Counter
    cnt = Counter()
    for i in range(n+1):
        cnt[sum_a[i]%m] += 1
    ans = 0
    for v in cnt.values():
        ans += v*(v-1)//2
    print(ans)

=======
Suggestion 10

def calc_divisible_count(numbers, div):
    count = 0
    sum = 0
    remainder_dict = {}
    for number in numbers:
        sum += number
        remainder = sum % div
        if remainder == 0:
            count += 1
        if remainder in remainder_dict:
            remainder_dict[remainder] += 1
        else:
            remainder_dict[remainder] = 1
    for remainder in remainder_dict:
        count += remainder_dict[remainder] * (remainder_dict[remainder] - 1) // 2
    return count
