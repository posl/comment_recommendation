Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

=======
Suggestion 2

def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    ans = 0
    for i in range(1, 10**6):
        cnt = 0
        for j in range(i, 10**6+1, i):
            cnt += c[j]
        if cnt == 1:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] != A[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i == 0:
            if A[i] != A[i+1]:
                ans += 1
        elif i == N-1:
            if A[i] != A[i-1]:
                ans += 1
        else:
            if A[i] != A[i-1] and A[i] != A[i+1]:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i == 0 or A[i] > A[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    # 素因数分解
    def prime_factorize(n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a

    # 素因数のリストを作成
    prime = []
    for i in range(N):
        prime += prime_factorize(A[i])
    prime = list(set(prime))

    # 素因数の個数をカウント
    count = {}
    for i in range(len(prime)):
        count[prime[i]] = 0

    for i in range(N):
        for j in range(len(prime)):
            if A[i] % prime[j] == 0:
                count[prime[j]] += 1

    # 素因数の個数が1であるものを数える
    ans = 0
    for i in range(len(prime)):
        if count[prime[i]] == 1:
            ans += 1

    print(ans)

=======
Suggestion 7

def  main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        elif A[i] != A[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    maxA = A[0]
    div = [0] * (maxA + 1)
    for i in range(N):
        div[A[i]] += 1
    for i in range(2, maxA + 1):
        for j in range(i, maxA + 1, i):
            div[i] += div[j]
    ans = 0
    for i in range(N):
        if div[A[i]] == 1:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    # Read input
    N = int(input())
    A = list(map(int, input().split()))
    # Count the number of occurrences of each number
    # (use a dictionary for this)
    count = {}
    for a in A:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    # Check which numbers are divisible by other numbers
    # (use a dictionary for this)
    div = {}
    for a in A:
        for i in range(2, int(a**0.5)+1):
            if a % i == 0:
                if a in div:
                    div[a] = True
                elif i in count:
                    div[a] = True
                elif a//i in count:
                    div[a] = True
    # Count the result
    res = 0
    for a in A:
        if a not in div:
            res += count[a]
    print(res)
