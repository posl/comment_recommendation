Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[2]-A[1] == A[1]-A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def solve():
    a = list(map(int, input().split()))
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    A = list(map(int,input().split()))
    A.sort()
    if A[0]+A[2] == 2*A[1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    A = list(map(int, input().split()))
    if len(set(A)) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    A = list(map(int, input().split()))
    if A[0] == A[1] == A[2]:
        print('Yes')
        return
    if A[0] == A[1] or A[1] == A[2] or A[0] == A[2]:
        print('No')
        return
    if A[0] + A[2] == 2 * A[1]:
        print('Yes')
        return
    print('No')
