Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] >> i & 1:
                cnt += 1
        ans += cnt * (n - cnt) * (1 << i)
        ans %= 10**9 + 7
    print(ans)

=======
Suggestion 2

def XOR(a,b):
    a = bin(a)[2:]
    b = bin(b)[2:]
    if len(a)>len(b):
        b = '0'*(len(a)-len(b))+b
    else:
        a = '0'*(len(b)-len(a))+a
    c = ''
    for i in range(len(a)):
        if a[i]=='1' and b[i]=='1':
            c += '0'
        elif a[i]=='0' and b[i]=='0':
            c += '0'
        else:
            c += '1'
    return int(c,2)

N = int(input())
A = list(map(int,input().split()))
mod = 10**9+7
ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        ans += XOR(A[i],A[j])
        ans %= mod
print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    mod = 10**9 + 7
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] >> i & 1:
                cnt += 1
        ans += (cnt * (N - cnt) * (1 << i)) % mod
    print(ans % mod)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & (1 << i):
                cnt += 1
        ans += (1 << i) * (cnt * (n - cnt))
        ans %= (10 ** 9 + 7)
    print(ans)
main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        ans += (cnt * (n - cnt) * (1 << i))
    print(ans % (10 ** 9 + 7))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if(a[j] >> i & 1):
                cnt += 1
        ans += cnt * (n - cnt) * (1 << i)
        ans %= mod
    print(ans)

=======
Suggestion 7

def solve(n, a):
    ans = 0
    for i in range(60):
        c = 0
        for j in range(n):
            if a[j] & 1:
                c += 1
            a[j] >>= 1
        ans += c * (n - c) * (1 << i)
        ans %= 10 ** 9 + 7
    return ans

=======
Suggestion 8

def problem147d():
    return

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & (1 << i):
                cnt += 1
        ans += cnt * (n - cnt) * (1 << i)
    print(ans % (10 ** 9 + 7))
