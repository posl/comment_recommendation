Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n-1):
        b[a[i]-1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 2

def get_subordinates_num(n, superiors):
    subordinates = [0] * n
    for i in superiors:
        subordinates[i - 1] += 1
    return subordinates

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #print(N)
    #print(A)

    #print(len(A))
    #print(len(A) + 1)

    #print(len(A) + 1)
    #print([0] * (len(A) + 1))

    B = [0] * (len(A) + 1)

    #print(B)

    for i in range(1, len(A)):
        B[A[i]] += 1

    #print(B)

    for i in range(1, len(B)):
        print(B[i])

=======
Suggestion 4

def getSubordinateNums(a, n):
    # a: list of int
    # n: int
    # return: list of int
    # return the number of direct subordinates of each member
    # a[i] is the direct superior of i+1
    # a[0] is the direct superior of 1
    # a[1] is the direct superior of 2
    # a[n-1] is the direct superior of n
    # a[i] < i+1
    # a[0] = 1
    # a[i] = i+1 is not allowed
    # i+1 is the member id
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    subNums = [0] * n
    for i in range(1, n):
        subNums[a[i]-1] += 1
    return subNums

=======
Suggestion 5

def countSubordinates(i, subordinates):
    if len(subordinates[i]) == 0:
        return 0
    else:
        result = len(subordinates[i])
        for sub in subordinates[i]:
            result += countSubordinates(sub, subordinates)
        return result

=======
Suggestion 6

def main():
    import sys
    import numpy as np
    input = sys.stdin.readline
    N = int(input())
    A = [int(x) for x in input().split()]
    A = np.array(A)
    A = np.sort(A)
    B = np.bincount(A)
    for i in range(1, N+1):
        print(B[i])

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(1, n):
        b[a[i-1]-1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[a[i]] += 1
    for i in range(1, n + 1):
        print(b[i])
