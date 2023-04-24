Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += 1/A[i]
    print(1/sum)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += 1/a[i]
    print(1/sum)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        ans += 1/a[i]
    print(1/ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [1/a for a in A]
    print(1/sum(B))

=======
Suggestion 5

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    inv_sum = 0
    for A in As:
        inv_sum += 1/A

    # output
    print(1/inv_sum)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(1/sum(1/x for x in A))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum([1 / x for x in a]))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1/(sum([1/i for i in a])))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = sum(1/a for a in A)
    print(1/ans)
