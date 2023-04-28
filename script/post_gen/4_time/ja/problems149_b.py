Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, k = map(int, input().split())
    if k >= a:
        k -= a
        a = 0
    else:
        a -= k
        k = 0
    if k >= b:
        k -= b
        b = 0
    else:
        b -= k
        k = 0
    print(a, b)

=======
Suggestion 2

def main():
    a, b, k = map(int, input().split())
    if a >= k:
        print(a - k, b)
    elif a + b >= k:
        print(0, b - (k - a))
    else:
        print(0, 0)

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    if K <= A:
        A -= K
    else:
        K -= A
        A = 0
        if K <= B:
            B -= K
        else:
            B = 0
    print(A, B)

=======
Suggestion 4

def main():
    a,b,k = map(int,input().split())
    for i in range(k):
        if i%2 == 0:
            if a%2 == 1:
                a -= 1
            b += a//2
            a //= 2
        else:
            if b%2 == 1:
                b -= 1
            a += b//2
            b //= 2
    print(a,b)

=======
Suggestion 5

def main():
    A, B, K = map(int, input().split())

    if K <= A:
        A = A - K
    elif K <= A + B:
        B = B - (K - A)
        A = 0
    else:
        A = 0
        B = 0

    print(A, B)

=======
Suggestion 6

def main():
    A, B, K = map(int, input().split())
    if K <= A:
        print(A - K, B)
    else:
        print(0, max(0, B - (K - A)))

=======
Suggestion 7

def main():
    A, B, K = map(int, input().split())
    if K <= A:
        print(A - K, B)
    else:
        print(0, B - (K - A))

=======
Suggestion 8

def main():
    a, b, k = map(int, input().split())

    if a >= k:
        a -= k
    else:
        b -= (k - a)
        a = 0

    if b < 0:
        b = 0

    print(a, b)

=======
Suggestion 9

def calc(a, b, k):
    if a >= k:
        a -= k
        return a, b
    else:
        b -= (k - a)
        a = 0
        if b >= 0:
            return a, b
        else:
            b = 0
            return a, b

=======
Suggestion 10

def solve(a,b,k):
    if k <= a:
        return (a-k,b)
    elif k <= a+b:
        return (0,a+b-k)
    elif k > a+b:
        return (0,0)

a,b,k = map(int,input().split())
ans = solve(a,b,k)
print(ans[0],ans[1])
