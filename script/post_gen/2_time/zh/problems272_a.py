Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a))

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a))

=======
Suggestion 3

def main():
    num = int(input())
    number = input().split()
    sum = 0
    for i in range(num):
        sum += int(number[i])
    print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    a = input().split()
    sum = 0
    for i in range(n):
        sum += int(a[i])
    print(sum)

=======
Suggestion 5

def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    #process
    ans = 0
    for i in range(N):
        ans += A[i]
    #output
    print(ans)

=======
Suggestion 6

def sum():
    n = int(input())
    num_list = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        sum += num_list[i]
    print(sum)

sum()
