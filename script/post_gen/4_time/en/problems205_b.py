Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] != i+1:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(1, N+1):
        if A[i-1] != i:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A == list(range(1,N+1)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A == [i for i in range(1, N+1)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(n):
        if a[i] != i + 1:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == n:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    for i in range(1,N+1):
        if A[i-1] != i:
            print('No')
            return
    print('Yes')

=======
Suggestion 8

def is_permutation(n, a):
    if n != len(a):
        return False
    a.sort()
    for i in range(1, n+1):
        if i != a[i-1]:
            return False
    return True

=======
Suggestion 9

def check_permutation(a):
    a.sort()
    if a[0] == 1:
        for i in range(len(a)-1):
            if a[i+1] - a[i] != 1:
                return "No"
        return "Yes"
    else:
        return "No"

=======
Suggestion 10

def check_permutation(n, a):
    a.sort()
    for i in range(n):
        if a[i] != i+1:
            return "No"
    return "Yes"
