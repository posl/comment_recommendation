Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
    from collections import Counter
    cnt = Counter()
    for a in A:
        cnt[a%M] += 1
    ans = 0
    for v in cnt.values():
        ans += v*(v-1)//2
    print(ans)

=======
Suggestion 2

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # 1 から n までの累積和
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]

    # s[r] - s[l] が m の倍数となる組 (l, r) を求める
    # その個数を ans に加算する
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for r in range(n + 1):
        ans += d[s[r] % m]
        d[s[r] % m] += 1

    print(ans)

solve()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] % M == 0:
            A[i] = int(A[i] / M)
        else:
            A[i] = A[i] % M
    for i in range(1, N):
        A[i] = A[i] + A[i - 1]
    A = [0] + A
    B = [0] * M
    for i in range(N + 1):
        B[A[i] % M] += 1
    ans = 0
    for i in range(M):
        ans += B[i] * (B[i] - 1) // 2
    print(ans)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    MOD = M
    from collections import defaultdict
    d = defaultdict(int)
    for s in S:
        d[s % MOD] += 1
    ans = 0
    for k, v in d.items():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 5

def get_divisor(n):
    divisor = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divisor.append(i)
            if i != n//i:
                divisor.append(n//i)
    return divisor

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,M,A)
    #print(len(A))
    #print(A[0],A[1],A[2])
    #print(A[1]+A[2])
    #print(A[0]+A[1]+A[2])
    #print(A[0]+A[1]+A[2]+A[3])
    #print(A[0]+A[1]+A[2]+A[3]+A[4])
    #print(A[1]+A[2]+A[3]+A[4])
    #print(A[2]+A[3]+A[4])
    #print(A[3]+A[4])
    #print(A[4])
    #print(A[2]+A[3])
    #print(A[1]+A[2])
    #print(A[0]+A[1])
    #print(A[1]+A[2]+A[3])
    #print(A[0]+A[1]+A[2])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8]+A[9])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8]+A[9]+A[10])
    #print(A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8]+A[9]+A[

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x % m for x in a]
    for i in range(n - 1):
        a[i + 1] += a[i]
        a[i + 1] %= m
    from collections import defaultdict
    d = defaultdict(int)
    d[0] = 1
    ans = 0
    for x in a:
        ans += d[x]
        d[x] += 1
    print(ans)

main()

=======
Suggestion 8

def get_num_divisible_by_m(num, m):
    if num < m:
        return 0
    else:
        return num // m

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a = [0] + a
    for i in range(n):
        a[i+1] += a[i]
    a = [i%m for i in a]
    from collections import Counter
    c = Counter(a)
    ans = 0
    for i in c:
        ans += c[i]*(c[i]-1)//2
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = sum_A[i] + A[i]
    sum_A = [a % M for a in sum_A]
    cnt = {}
    for a in sum_A:
        if a in cnt:
            cnt[a] += 1
        else:
            cnt[a] = 1
    ans = 0
    for c in cnt.values():
        ans += c * (c - 1) // 2
    print(ans)
