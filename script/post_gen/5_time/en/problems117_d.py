Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        cnt = 0
        for a in A:
            if a >> i & 1:
                cnt += 1
        if cnt < N - cnt and ans + (1 << i) <= K:
            ans += 1 << i
    f = 0
    for a in A:
        f += ans ^ a
    print(f)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(50, -1, -1):
        c = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                c += 1
        if c <= n / 2 and ans + (1 << i) <= k:
            ans += (1 << i)
    f = 0
    for i in range(n):
        f += ans ^ a[i]
    print(f)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        if (k >> i) & 1:
            x = 0
            for j in range(n):
                if (a[j] >> i) & 1:
                    x += 1 << i
                else:
                    x += a[j] & ((1 << i) - 1)
            ans = max(ans, x)
        else:
            x = 0
            for j in range(n):
                if (a[j] >> i) & 1:
                    x += a[j] & ((1 << i) - 1)
                else:
                    x += 1 << i
            ans = max(ans, x)
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * 41
    for i in range(41):
        for j in range(n):
            if a[j] >> i & 1:
                b[i] += 1
    c = 0
    for i in range(40, -1, -1):
        if c + 2 ** i <= k:
            if b[i] > n - b[i]:
                c += 2 ** i
        else:
            if b[i] <= n - b[i]:
                c += 2 ** i
    d = 0
    for i in range(n):
        d += c ^ a[i]
    print(d)

=======
Suggestion 5

def xor_sum(n, k, a):
    max_f = 0
    for i in range(k+1):
        f = 0
        for j in range(n):
            f += i ^ a[j]
        if f > max_f:
            max_f = f
    return max_f

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = 0

    for i in range(K.bit_length(), -1, -1):
        count = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                count += 1

        if count < N - count and result + (1 << i) <= K:
            result += 1 << i

    for i in range(N):
        result += A[i] ^ result

    print(result)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(40, -1, -1):
        if k & (1 << i):
            tmp = 0
            for j in range(n):
                if a[j] & (1 << i):
                    tmp += 1 << i
                else:
                    if tmp + (1 << i) <= k:
                        tmp += 1 << i
            k = tmp
    ans = 0
    for i in range(n):
        ans += k ^ a[i]
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    max_bit = 1
    for i in range(1, 41):
        if k < max_bit:
            break
        max_bit *= 2
    max_bit //= 2
    bit = 0
    ans = 0
    while max_bit > 0:
        count = 0
        for i in range(n):
            if a[i] & max_bit:
                count += 1
        if count < n - count and bit + max_bit <= k:
            bit += max_bit
        ans += max_bit * (n - count if count < n - count else count)
        max_bit //= 2
    print(ans)

=======
Suggestion 9

def solve():
    #n,k=map(int,input().split())
    #a=list(map(int,input().split()))
    n,k=3,7
    a=[1,6,3]
    b=bin(k)
    c=len(b)-2
    d=[0]*c
    for i in range(c):
        for j in range(n):
            d[i]+=((a[j]>>i)&1)
    ans=0
    for i in range(c-1,-1,-1):
        if d[i]<n/2:
            if ans+(1<<i)<=k:
                ans+=(1<<i)
    e=0
    for i in range(n):
        e+=ans^a[i]
    print(e)
    return 0

=======
Suggestion 10

def solve(N, K, A):
    # write your code here
    print(N, K, A)
    return 0
