Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A) - N)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a) - n)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += N*(A[i+1]-A[i])
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    print(sum(A)-N)

=======
Suggestion 6

def max_f(a):
    return sum(a) - len(a)
