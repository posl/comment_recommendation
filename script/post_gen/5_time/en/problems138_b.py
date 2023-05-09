Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += 1/a[i]
    print(1/sum)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += 1 / A[i]
    print(1 / sum)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1/sum(map(lambda x: 1/x, a)))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = 0

    for i in range(n):
        result += 1 / a[i]

    print(1 / result)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum_inv_a = 0
    for i in range(n):
        sum_inv_a += 1/a[i]
    print(1/sum_inv_a)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1/sum(list(map(lambda x: 1/x, a))))

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(1/sum([1/i for i in A]))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
    else:
        print(1 / sum([1 / a for a in A]))

=======
Suggestion 9

def main():
    n = int(input())
    a = map(int, input().split())
    print(1 / sum(map(lambda x: 1 / x, a)))

=======
Suggestion 10

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum([1 / x for x in a]))
