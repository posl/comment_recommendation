Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    num_list = list(map(int, input().split()))
    num_set = set(num_list)
    if len(num_list)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:
            prin

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) == len(set(a)):
        print("YES")
    else:
        print("NO")

=======
Suggestion 4

def check_pair(n, a):
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            return False
    return True

=======
Suggestion 5

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            pri

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(1,n):
        if a[i-1] == a[i]:
            print
