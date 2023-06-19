Synthesizing 10/10 solutions (Duplicates hidden)

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
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    for i in range(n):
        result += 1 / a[i]
    print(1 / result)

=======
Suggestion 3

def main():
    N = int(input())
    A = input().split()
    A = [int(i) for i in A]
    result = 0
    for i in range(N):
        result += 1/A[i]
    print(1/result)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1/sum([1/x for x in a]))

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    print(1 / sum([1 / a for a in A]))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum(1 / i for i in a))

=======
Suggestion 7

def main():
    N = input()
    A = input()
    print(1/sum([1/int(i) for i in A.split()]))
main()

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += 1 / a[i]
    print(1 / ans)
