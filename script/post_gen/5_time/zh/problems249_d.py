Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A_set = set(A)
    A_dict = {}
    for a in A:
        if a not in A_dict:
            A_dict[a] = 1
        else:
            A_dict[a] += 1
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] * A[j] in A_set:
                ans += A_dict[A[i] * A[j]]
    print(ans)

=======
Suggestion 2

def get_divisor(n):
    i = 1
    res = []
    while i*i <= n:
        if n%i == 0:
            res.append(i)
            if i != n//i:
                res.append(n//i)
        i += 1
    res.sort()
    return res

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    max_a = max(a)
    #print(max_a)
    cnt = [0]*(max_a+1)
    for i in range(1, n+1):
        cnt[a[i]] += 1
    #print(cnt)
    ans = 0
    for i in range(1, max_a+1):
        for j in range(i, max_a+1, i):
            if cnt[j] == 0:
                continue
            if i == j:
                ans += cnt[i]*(cnt[i]-1)*(cnt[i]-2)//6
            elif i < j:
                k = j-i
                if k > max_a:
                    continue
                ans += cnt[i]*cnt[j]*cnt[k]
    print(ans)
    return

=======
Suggestion 4

def gongyinshu(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

=======
Suggestion 5

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

N = int(input())
A = list(map(int, input().split()))
A.sort()
dict = {}
for i in range(N):
    if A[i] in dict:
        dict[A[i]] += 1
    else:
        dict[A[i]] = 1

ans = 0
for i in range(N):
    divisors = make_divisors(A[i])
    for j in range(len(divisors)):
        if divisors[j] in dict:
            ans += dict[divisors[j]]
            if A[i] == divisors[j]:
                ans -= 1
print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(len(A))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] % A[j] != 0:
                continue
            for k in range(N):
                if j == k:
                    continue
                if A[j] % A[k] != 0:
                    continue
                ans += 1
    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (max(a) + 1)
    for i in range(n):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, max(a) + 1):
        for j in range(i, max(a) + 1, i):
            ans += cnt[i] * cnt[j] * (cnt[j // i])
        ans -= cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
    print(ans)

=======
Suggestion 8

def solve(n, a):
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n):
        d[a[i]] += 1
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] * a[j] in d:
                ans += d[a[i]*a[j]]
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 9

def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

=======
Suggestion 10

def calc():
    n = int(input())
    a = [int(x) for x in input().split()]
    d = dict()
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if a[j] == 0:
                continue
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] in d:
                ans += d[a[i] // a[j]]
    print(ans)

calc()
