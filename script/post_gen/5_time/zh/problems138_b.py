Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += 1 / a[i]
    print(1 / sum)

=======
Suggestion 2

def problems138_b():
    pass

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in a:
        sum += 1/i
    print(1/sum)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum([1 / i for i in a]))

=======
Suggestion 5

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += 1 / a_list[i]
    print(1 / sum)

=======
Suggestion 6

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in a:
        sum += 1/i
    print(1/sum)
solve()

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum(1 / ai for ai in a))
