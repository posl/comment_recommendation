Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * 10 ** 5 + 1)
    for a in A:
        B[a] += 1
    ans = 0
    for i in range(1, 2 * 10 ** 5 + 1):
        if B[i] == 0:
            continue
        for j in range(i, 2 * 10 ** 5 + 1, i):
            if B[j] == 0:
                continue
            if i == j:
                ans += B[i] * (B[i] - 1) // 2
            else:
                ans += B[i] * B[j]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * 10**5 + 1)
    for a in A:
        B[a] += 1
    ans = 0
    for i in range(1, 2 * 10**5 + 1):
        if B[i] == 0:
            continue
        for j in range(1, 2 * 10**5 // i + 1):
            if B[j] == 0:
                continue
            if i == j:
                ans += (B[i] * (B[i] - 1) * (B[i] - 2)) // 6
            elif i < j:
                ans += B[i] * B[j] * (B[i * j] - B[i] - B[j] + 1)
            else:
                ans += B[i] * B[j] * (B[i * j] - B[i] - B[j])
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] % A[j] == 0:
                ans += 1
    print(ans)

main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] * A[j] > 2 * 10**5:
                break
            ans += A.count(A[i] * A[j])
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] * a[j] > 2 * 10 ** 5:
                break
            ans += bisect.bisect_right(a, a[i] * a[j]) - j - 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (A[-1] + 1)
    for i in range(N):
        B[A[i]] += 1
    ans = 0
    for i in range(N):
        for j in range(A[i], A[-1] + 1, A[i]):
            ans += B[j]
        B[A[i]] -= 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i] % a[j] == 0:
                for k in range(n):
                    if a[k] == a[i] / a[j]:
                        ans += 1
    print(ans)

=======
Suggestion 8

def divisors(n):
    """nの約数を列挙"""
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    A.append(0)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i]%A[j] == 0:
                ans += A.count(A[i]//A[j])
    print(ans)
