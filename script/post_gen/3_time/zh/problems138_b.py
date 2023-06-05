Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1/sum([1/i for i in a]))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in a:
        sum += 1/i
    print(1/sum)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(1 / sum(map(lambda x: 1 / x, A)))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += 1/a[i]
    print(1/sum)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum([1 / x for x in a]))
