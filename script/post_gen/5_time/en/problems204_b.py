Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > 10:
            ans += A[i] - 10
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        if A[i] > 10:
            total += A[i] - 10
    print(total)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] > 10:
            count += a[i] - 10
    print(count)

=======
Suggestion 4

def harvest_nuts(nuts):
    total_nuts = 0
    for nut in nuts:
        if nut > 10:
            total_nuts += nut - 10
    return total_nuts

=======
Suggestion 5

def problem204_b():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n):
        if a[i] > 10:
            total += a[i] - 10
    print(total)

=======
Suggestion 6

def harvest_nuts(trees):
    nuts = 0
    for tree in trees:
        if tree > 10:
            nuts += tree - 10
    return nuts

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    total = 0
    for i in range(n):
        if a[i] > 10:
            total += a[i] - 10
    print(total)

=======
Suggestion 8

def main():
    num = int(input())
    nuts = list(map(int, input().split()))
    total = 0
    for n in nuts:
        if n > 10:
            total += n - 10
    print(total)
