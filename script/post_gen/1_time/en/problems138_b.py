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
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        ans += 1/a
    print(1/ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))

    sum_inv = 0
    for a in A:
        sum_inv += 1/a

    print(1/sum_inv)

main()

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    print(1/sum([1/a for a in A]))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(1 / sum([1 / a for a in A]))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(1/sum([1/i for i in A]))

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    print(1/sum(1/a for a in A))

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    print(sum([1/a for a in A])**-1)
