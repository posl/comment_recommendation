Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = (S[i] + A[i]) % M
    from collections import Counter
    C = Counter(S)
    ans = 0
    for v in C.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    d = {}
    for i in range(n+1):
        r = s[i] % m
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    ans = 0
    for v in d.values():
        ans += v * (v-1) // 2
    print(ans)

main()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] = (A[i-1] + A[i]) % M
    from collections import defaultdict
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    ans = 0
    for k in d:
        ans += d[k] * (d[k] - 1) // 2
    print(ans)

=======
Suggestion 4

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N+1):
        d[S[i]%M] += 1
    ans = 0
    for k,v in d.items():
        ans += v*(v-1)//2
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    d = {}
    for i in range(n + 1):
        r = s[i] % m
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x % m for x in a]
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = (s[i] + a[i]) % m
    from collections import Counter
    c = Counter(s)
    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 7

def get_input():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    return n, m, a

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    #累積和を求める
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = (s[i] + A[i]) % M

    #累積和をソートする
    s.sort()

    ans = 0
    #s[i] == s[i + 1] となる要素の個数を求める
    cnt = 1
    for i in range(N):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

main()

=======
Suggestion 9

def countSubarrays(arr, n, m): 
    mod = [0] * m 
  
    cumSum = 0
    for i in range(n): 
        cumSum = (cumSum + arr[i]) % m 
        mod[cumSum] += 1
  
    result = 0 
    for i in range(m): 
        if (mod[i] > 1): 
            result += (mod[i] * (mod[i] - 1)) // 2
  
    result += mod[0] 
    return result 
  
n, m = map(int, input().split()) 
arr = list(map(int, input().split())) 
  
print(countSubarrays(arr, n, m))

=======
Suggestion 10

def main():
    from sys import stdin
    from collections import defaultdict

    n,m = map(int,stdin.readline().strip().split())
    a = list(map(int,stdin.readline().strip().split()))

    s = [0]
    for i in range(n):
        s.append((s[i]+a[i])%m)

    d = defaultdict(int)
    for i in range(n+1):
        d[s[i]] += 1

    ans = 0
    for k,v in d.items():
        ans += v*(v-1)//2

    print(ans)

main()
