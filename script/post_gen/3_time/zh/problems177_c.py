Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            ans += A[i]*A[j]
    print(ans%(10**9+7))

=======
Suggestion 2

def sum_of_products(arr):
    sum = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            sum += arr[i]*arr[j]
    return sum

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    ans = 0
    for i in range(n):
        sum -= a[i]
        ans += sum * a[i]
    print(ans % (10**9+7))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    S = sum(A)
    ans = 0
    for i in range(N):
        S -= A[i]
        ans += A[i] * S
        ans %= MOD
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    nums = [int(i) for i in input().split()]
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += nums[i] * nums[j]
    print(sum % (10**9+7))

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    sum = 0
    for i in range(n):
        for j in range(i+1,n):
            sum = (sum + a[i]*a[j])%(10**9+7)
    print(sum)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))

    mod = 10**9 + 7
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += a[i] * a[j]
            ans %= mod

    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += A[i] * A[j]
            sum %= MOD
    print(sum)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    sum_A = sum(A)
    sum_A2 = sum([a*a for a in A])
    print((sum_A*sum_A-sum_A2)//2%MOD)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
    print(ans % (10**9 + 7))
