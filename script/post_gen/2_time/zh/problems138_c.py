Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum(map(lambda x: 1 / x, a)))

main()

=======
Suggestion 2

def main():
    a = int(input())
    b = list(map(int,input().split()))
    c = 0
    for i in b:
        c += 1/i
    print(1/c)
main()

=======
Suggestion 3

def problems138_b():
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    for i in a:
        result += 1/i
    print(1/result)
problems138_b()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += 1 / a[i]
    print(1 / sum)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum([1 / ai for ai in a]))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(lambda x: 1/x, a))
    print(1/sum(b))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += 1 / A[i]
    print(1 / sum)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [1/i for i in A]
    print(1/sum(A))
