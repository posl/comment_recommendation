Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[i] = a[i] // 2
    a.sort(reverse=True)
    print(sum(a))

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        A[i] = A[i] // 2
    A.sort(reverse=True)
    print(sum(A))

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        A[i] //= 2
    A.sort(reverse=True)
    return sum(A)

print(solve())

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    i = 0
    while i < m and a[i] >= a[0] / (2 ** (i + 1)):
        i += 1
    print(sum(a[i:]) + a[0] * (2 ** (i + 1) - 1))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(0, N):
        sum += A[i]
    for i in range(0, M):
        sum = sum // 2
    print(sum)

=======
Suggestion 6

def get_input():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    return n, m, a

=======
Suggestion 7

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    a.append(0)
    ans = 0
    for i in range(n):
        if a[i] <= a[i+1]:
            ans += a[i]
        else:
            ans += a[i]//2**(m)
            m -= 1
            if m == 0:
                break
    print(ans)

=======
Suggestion 8

def main():
    #n, m = [int(x) for x in input().split()]
    #a = [int(x) for x in input().s

=======
Suggestion 9

def get_input():
    return list(map(int, input().split()))
