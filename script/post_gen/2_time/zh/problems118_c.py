Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def min_health(monster):
    monster.sort()
    for i in range(len(monster)-1):
        if monster[i+1] % monster[i] == 0:
            monster[i+1] = monster[i]
    return monster[-1]

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(min(A))

=======
Suggestion 3

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

=======
Suggestion 4

def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [2, 10, 8, 40]
    # A = [5, 13, 8, 1000000000]
    # A = [1000000000, 1000000000, 1000000000]
    # N = 4
    # N = 3
    # N = 4
    # A = [2, 10, 8, 40]
    # A = [5, 13, 8, 1000000000]
    # A = [1000000000, 1000000000, 1000000000]
    # N = 3
    # A = [1000000000, 1000000000, 1000000000]
    # N = 2
    # A = [1000000000, 1000000000]
    # N = 5
    # A = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    # N = 10
    # A = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000,
    #      1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    # N = 100000
    # A = [1000000000] * 100000
    # N = 10
    # A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]
    # N = 10
    # A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 999999999]
    # N = 10
    # A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 999999998]
    # N = 10
    # A = [1, 1, 1, 1, 1,

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))

    while len(a) > 1:
        a.sort()
        a[-1] -= a[0]
        a.pop(0)
        if a[-1] == 0:
            a.pop()

    print(a[0])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(1, N):
        A[i] %= A[0]
        if A[i] == 0:
            A[i] = A[0]
    A[0] = 0
    A.sort()
    print(A[0])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = a[0]
    for i in range(1, n):
        if ans * 2 >= a[i]:
            ans += a[i]
        else:
            ans = a[i]
    print(ans)

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
