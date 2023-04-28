Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A))

=======
Suggestion 3

def main():
    # input
    n = int(input())
    a = list(map(int, input().split()))

    # compute
    sum = 0
    for i in range(n):
        sum += a[i]

    # output
    print(sum)
