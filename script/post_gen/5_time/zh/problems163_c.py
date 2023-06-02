Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0] * n
    for i in range(n-1):
        B[A[i]-1] += 1
    for i in range(n):
        print(B[i])

=======
Suggestion 2

def getSubordinateNumber(n, a):
    subordinateNumber = [0] * n
    for i in range(n - 1):
        subordinateNumber[a[i] - 1] += 1
    return subordinateNumber

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(1, N):
        B[A[i] - 1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 4

def count_subordinates(n, A):
    subordinates = [0] * n
    for i in range(1, n):
        subordinates[A[i-1]-1] += 1
    return subordinates

=======
Suggestion 5

def get_subordinate_num(N, A):
    subordinate_num = [0] * N
    for i in range(1, N):
        subordinate_num[A[i-1]-1] += 1
    return subordinate_num

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(n - 1):
        b[a[i] - 1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 1からNまでの各社員の直属の部下の数を数える
    ans = [0] * N
    for i in range(1, N):
        ans[A[i - 1] - 1] += 1

    for i in range(N):
        print(ans[i])

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*N
    for i in range(1,N):
        B[A[i-1]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 9

def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    N = 7
    A = [1, 2, 3, 4, 5, 6]
    B = [0] * N
    for i in range(1, N):
        B[A[i] - 1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 10

def find_subordinates(n, boss):
    subordinates = [0 for i in range(n)]
    for i in range(1, n):
        subordinates[boss[i]-1] += 1
    return subordinates
