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
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    for i in range(N):
        result += 1/A[i]
    print(1/result)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += 1 / a[i]
    print(1 / sum)
main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1/sum([1/x for x in a]))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    sum = 0
    for i in range(N):
        sum += 1/A[i]
    print(1/sum)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum([1 / i for i in a]))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_inv = [1/a for a in A]
    A_inv_sum = sum(A_inv)
    print(1/A_inv_sum)

main()  # コード提出時にはコメントアウト

=======
Suggestion 8

def getInverseSum(n, a):
    sum = 0
    for i in range(n):
        sum += 1/a[i]
    return 1/sum
