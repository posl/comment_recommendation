Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n+1):
        if a[i-1] != i:
            print('No')
            return
    print('Yes')

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == [i for i in range(1, n+1)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if A[i] != i+1:
            print('No')
            break
    else:
        print('Yes')

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n == len(set(a)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def problem205_b():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(n):
        if a[i] != i+1:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 6

def check_permutation():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n+1):
        if i != a[i-1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 7

def check_permutation(n, a):
    a.sort()
    for i in range(n):
        if i+1 != a[i]:
            return 'No'
    return 'Yes'

=======
Suggestion 8

def main():
    # Get the number of integers in the sequence.
    n = int(input())
    # Get the sequence of integers.
    a = input().split()
    # Convert the sequence of integers from strings to integers.
    a = [int(x) for x in a]
    # Sort the sequence of integers.
    a.sort()
    # Check if the sequence of integers is a permutation of (1, 2, ..., N).
    if a == list(range(1, n + 1)):
        # If the sequence of integers is a permutation of (1, 2, ..., N), print Yes.
        print("Yes")
    else:
        # If the sequence of integers is not a permutation of (1, 2, ..., N), print No.
        print("No")

=======
Suggestion 9

def is_permutation(A):
    return len(set(A)) == len(A) and max(A) == len(A)
