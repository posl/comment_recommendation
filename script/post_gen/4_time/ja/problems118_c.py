Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

N = int(input())
A = list(map(int, input().split()))

=======
Suggestion 3

def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    n = 3
    a = [1000000000, 1000000000, 1000000000]
    a.sort()
    while True:
        if len(a) == 1:
            break
        if a[-1] == a[-2]:
            a[-2] = a[-1] = a[-1] // 2
            a.sort()
        else:
            a[-1] = a[-1] - a[-2]
            a.sort()
    print(a[0])

main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    while len(a) > 1:
        a.sort()
        a[-1] = a[-1] % a[0]
        if a[-1] == 0:
            a.pop()
    print(a[0])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    while len(a) > 1:
        a.sort()
        if a[-1] != a[-2]:
            a[-1] -= a[-2]
            a.pop(-2)
        else:
            a.pop(-1)
    print(a[0])

=======
Suggestion 6

def attack(a, b):
    if a > b:
        return a - b
    else:
        return b - a

N = int(input())
A = list(map(int, input().split()))

=======
Suggestion 7

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    while len(set(A)) > 1:
        A.sort()
        A[-1] = A[-1] % A[-2]
        A = list(set(A))

    print(A[0])

=======
Suggestion 9

def func(N, A):
    if N == 2:
        return min(A)
    min_A = min(A)
    max_A = max(A)
    if min_A == max_A:
        return min_A
    min_A_idx = A.index(min_A)
    max_A_idx = A.index(max_A)
    if min_A_idx > max_A_idx:
        min_A_idx, max_A_idx = max_A_idx, min_A_idx
    A[min_A_idx] = min_A
    A[max_A_idx] -= min_A
    return func(N, A)
