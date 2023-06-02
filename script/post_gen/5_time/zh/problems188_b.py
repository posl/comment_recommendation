Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum([a[i] * b[i] for i in range(n)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    inner_product = 0
    for i in range(N):
        inner_product += A[i] * B[i]
    if inner_product == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def problem188_b():
    pass

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i]*b[i] for i in range(n)]
    if sum(c) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    #input
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    #process
    result = 0
    for i in range(n):
        result += a_list[i] * b_list[i]
    #output
    if result == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    sum = 0
    for i in range(n):
        sum += a[i]*b[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")
