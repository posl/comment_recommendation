Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]

    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for i in range(n + 1):
        ans += d[s[i]]
        d[s[i] + k] += 1
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    d = {}
    for i in range(n + 1):
        if s[i] - k in d:
            ans += d[s[i] - k]
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    print(ans)

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = 0
    for i in range(N + 1):
        for j in range(i + 1, N + 1):
            if S[j] - S[i] == K:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for i in range(n + 1):
        ans += d[s[i]]
        d[s[i] + k] += 1
    print(ans)

=======
Suggestion 5

def main():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	s = [0] * (n + 1)
	for i in range(n):
		s[i + 1] = s[i] + a[i]
	#print(s)
	ans = 0
	r = 0
	for l in range(n):
		while r < n + 1 and s[r] - s[l] < k:
			r += 1
		if s[r] - s[l] == k:
			ans += 1
	print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(N):
        A[i+1] += A[i]
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for i in range(N+1):
        ans += d[A[i]-K]
        d[A[i]] += 1
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0]
    for a in A:
        S.append(S[-1] + a)
    from collections import defaultdict
    D = defaultdict(int)
    ans = 0
    for s in S:
        ans += D[s]
        D[s + K] += 1
    print(ans)

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    s = 0
    l = 0
    for r in range(N):
        s += A[r]
        while s >= K:
            if s == K:
                ans += 1
            s -= A[l]
            l += 1
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # Aの累積和
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])

    # 累積和の差分
    T = []
    for i in range(N+1):
        T.append(S[i] - K)

    # 累積和の差分の集合
    T = set(T)

    # 累積和の差分の集合に含まれる累積和の個数をカウント
    count = 0
    for i in range(N+1):
        if S[i] in T:
            count += 1
    print(count)

=======
Suggestion 10

def get_ints(): return map(int, input().strip().split())
