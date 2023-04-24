Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        for j in range(i+1, N):
            sum += A[i] ^ A[j]
    print(sum % (10**9+7))

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j]>>i & 1:
                cnt += 1
        ans = (ans + (1<<i) * cnt * (n-cnt)) % mod
    print(ans)

=======
Suggestion 3

def solve(N, A):
    # mod = 10**9 + 7
    # ans = 0
    # for i in range(N-1):
    #     for j in range(i+1, N):
    #         ans += A[i] ^ A[j]
    #         ans %= mod
    # return ans
    # print(A)
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        # print("i", i)
        count = 0
        for j in range(N):
            if A[j] & 1:
                count += 1
            A[j] >>= 1
        # print("count", count)
        ans += count * (N-count) * pow(2, i, mod)
        ans %= mod
    return ans

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        n1 = 0
        for j in range(n):
            if a[j] & (1 << i):
                n1 += 1
        ans += (n1 * (n - n1) * (1 << i))
    print(ans % (10 ** 9 + 7))

=======
Suggestion 5

def xor_sum(arr):
    xor_sum = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            xor_sum += arr[i]^arr[j]
    return xor_sum

=======
Suggestion 6

def xor_sum(n, a):
    sum = 0
    for i in range(n):
        for j in range(i + 1, n):
            sum += a[i] ^ a[j]
    return sum

n = int(input())
a = [int(x) for x in input().split()]
print(xor_sum(n, a) % (10**9 + 7))

=======
Suggestion 7

def xor_sum(A):
    total = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            total += A[i] ^ A[j]
    return total % (10**9+7)

N = int(input())
A = list(map(int, input().split()))
print(xor_sum(A))

=======
Suggestion 8

def xor_sum(n, a):
  s = 0
  for i in range(n-1):
    for j in range(i+1, n):
      s += a[i] ^ a[j]
  return s % (10**9+7)

=======
Suggestion 9

def xor_sum(N, A):
    s = 0
    for i in range(N):
        for j in range(i+1, N):
            s += A[i] ^ A[j]
    return s

=======
Suggestion 10

def XOR_sum(N, A):
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] >> i & 1:
                cnt += 1
        ans += (cnt * (N-cnt) * (1 << i)) % mod
    return ans % mod

N = int(input())
A = list(map(int, input().split()))
print(XOR_sum(N, A))
