Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for a in A:
        ans[a - 1] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [0] * N
    for i in range(1, N):
        B[A[i-1]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * N
    for i in range(N - 1):
        count[A[i] - 1] += 1
    for j in range(N):
        print(count[j])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n-1):
        b[a[i]-1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(1, N):
        B[A[i-1]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n-1):
        b[a[i]-1] += 1
    for i in b:
        print(i)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in a:
        ans[i - 1] += 1
    for i in ans:
        print(i)

=======
Suggestion 8

def count_subordinates(n, id_list):
    subordinate_count = [0] * n

    for i in range(n-1):
        subordinate_count[id_list[i]-1] += 1

    for i in range(n-1):
        subordinate_count[i] += subordinate_count[i+1]

    return subordinate_count

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in a:
        b[i-1] += 1
    for i in b:
        print(i)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(1, N):
        B[A[i] - 1] += 1
    for i in range(N):
        print(B[i])
