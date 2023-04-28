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
    result = 0
    for i in range(N):
        if A[i] > 10:
            result += A[i] - 10
    print(result)

=======
Suggestion 3

def harvest_nuts(trees):
    nuts = 0
    for tree in trees:
        if tree > 10:
            nuts += tree - 10
    return nuts

=======
Suggestion 4

def harvest(nuts):
    total = 0
    for nut in nuts:
        if nut > 10:
            total += nut - 10
    return total

=======
Suggestion 5

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))

    # compute
    nuts = 0
    for a in A:
        if a > 10:
            nuts += a - 10

    # output
    print(nuts)

=======
Suggestion 6

def harvest_nuts(nuts):
    total = 0
    for nut in nuts:
        if nut > 10:
            total += nut - 10
    return total

=======
Suggestion 7

def main():
    n = int(input())
    ai = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if ai[i] > 10:
            sum += ai[i] - 10
    print(sum)

=======
Suggestion 8

def harvest_nuts(n,a):
    total_nuts = 0
    for i in range(n):
        if a[i] > 10:
            total_nuts += a[i] - 10
    return total_nuts

n = int(input())
a = list(map(int, input().split()))
print(harvest_nuts(n,a))

=======
Suggestion 9

def get_nuts(nuts):
    nuts_taken = 0
    for nut in nuts:
        if nut <= 10:
            continue
        else:
            nuts_taken += nut - 10
    return nuts_taken
