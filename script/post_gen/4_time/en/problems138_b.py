Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += 1 / A[i]
    print(1 / sum)

=======
Suggestion 2

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    sum = 0
    for a in a_list:
        sum += 1/a
    print(1/sum)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        sum += 1/a[i]

    print(1/sum)

=======
Suggestion 4

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_sum = 0
    for a in a_list:
        a_sum += 1/a

    print(1/a_sum)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1/sum([1/x for x in a]))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1/sum([1/i for i in a]))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum(1 / x for x in a))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum([1 / ai for ai in a]))

=======
Suggestion 9

def inverse_sum(numbers):
    sum = 0
    for number in numbers:
        sum += 1/number
    return 1/sum
