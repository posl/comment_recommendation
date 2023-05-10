Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [1 / i for i in a]
    print(1 / sum(b))

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
    N = int(input())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += 1 / A[i]
    print(1 / total)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += 1/a[i]
    print(1/ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = 0
    for i in a:
        b += 1/i
    print(1/b)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_sum = 0
    for i in range(n):
        a_sum += 1 / a[i]

    print(1 / a_sum)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))

    print(1/sum([1/x for x in a]))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_inv = [1 / x for x in a]
    print(1 / sum(a_inv))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum(list(map(lambda x: 1 / x, a))))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(1/sum([1/a for a in A]))
