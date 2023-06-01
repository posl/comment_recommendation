Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    f = [0] * 41
    for i in range(41):
        for j in range(n):
            if a[j] & (1 << i):
                f[i] += 1
    ans = 0
    for i in range(40, -1, -1):
        if ans + (1 << i) <= k:
            ans += (1 << i) * max(f[i], n - f[i])
        else:
            ans += (1 << i) * f[i]
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    K = bin(K)[2:]
    K = '0' * (len(A) - len(K)) + K
    ans = 0
    for i in range(len(A)):
        if K[i] == '1':
            ans += A[i]
        else:
            ans += A[i] // 2
    print(ans)
main()

=======
Suggestion 3

def xor_sum(a, b):
    if a == b:
        return a
    if b - a == 1:
        return a ^ b
    if a % 2 == 0 and b % 2 == 0:
        return xor_sum(a // 2, b // 2) * 2
    if a % 2 == 0 and b % 2 == 1:
        return xor_sum(a // 2, b // 2) * 2 + 1
    if a % 2 == 1 and b % 2 == 0:
        return xor_sum((a + 1) // 2, b // 2) * 2
    if a % 2 == 1 and b % 2 == 1:
        return xor_sum((a + 1) // 2, b // 2) * 2 + 1

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(41, -1, -1):
    count = 0
    for j in range(n):
        if a[j] >> i & 1:
            count += 1
    if count <= n // 2:
        continue
    if ans + (1 << i) <= k:
        ans += 1 << i

s = 0
for i in range(n):
    s += ans ^ a[i]
print(s)

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    bit = 0
    for i in range(40, -1, -1):
        cnt = 0
        for a in A:
            if a >> i & 1:
                cnt += 1
        if cnt <= N - cnt and bit + (1 << i) <= K:
            bit += 1 << i
    ans = 0
    for a in A:
        ans += bit ^ a
    print(ans)

=======
Suggestion 5

def f(x, a):
    return sum([x ^ i for i in a])

=======
Suggestion 6

def f(x, a_list):
    res = 0
    for a in a_list:
        res += x ^ a
    return res

=======
Suggestion 7

def f(x, a):
    return sum([x ^ ai for ai in a])

=======
Suggestion 8

def f(x, arr):
    sum = 0
    for i in range(len(arr)):
        sum += x ^ arr[i]
    return sum

=======
Suggestion 9

def xor(a,b):
    a1 = bin(a)[2:]
    b1 = bin(b)[2:]
    if len(a1) > len(b1):
        b1 = '0'*(len(a1)-len(b1))+b1
    else:
        a1 = '0'*(len(b1)-len(a1))+a1
    result = ''
    for i in range(len(a1)):
        if a1[i] == b1[i]:
            result += '0'
        else:
            result += '1'
    return int(result,2)

N,K = map(int,input().strip().split())
A = list(map(int,input().strip().split()))
result = 0
for i in range(K+1):
    temp = 0
    for j in range(N):
        temp += xor(i,A[j])
    if temp > result:
        result = temp
print(result)
