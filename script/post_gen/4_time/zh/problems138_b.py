Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    for i in range(n):
        x += 1/a[i]
    print(1/x)

main()

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        sum += 1 / a[i]
    print(1 / sum)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    for i in range(n):
        result += 1 / a[i]
    print(1 / result)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = 0
    for i in range(n):
        b += 1 / a[i]
    print(1 / b)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += 1/A[i]
    print(1/sum)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum(1 / i for i in a))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum(map(lambda x: 1 / x, a)))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for i in a:
        total += 1 / i
    print(1 / total)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1/sum(list(map(lambda x: 1/x, a))))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += 1 / a[i]
    print(1 / ans)
