Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    for i in range(M):
        if A[i] < total / (4 * M):
            print('No')
            return
    print('Yes')

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    if a[m-1] >= sum(a) / (4*m):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[M-1] >= sum(A) / (4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total / (4*m):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    print('Yes' if A[M-1] >= total/(4*M) else 'No')

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] >= total / (4 * M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    votes = sum(A)
    threshold = votes // (4 * M)
    if A[M - 1] >= threshold:
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    sum_A = sum(A)
    A.sort(reverse=True)
    A = A[:M]

    if A[M-1] >= sum_A / (4 * M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    # Read from stdin
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # Calculate the total number of votes
    total_votes = sum(A)

    # Sort the votes
    A.sort(reverse=True)

    # Check if the M-th popular item has more than (1/(4M)) of the total number of votes
    if A[M-1] >= (total_votes / (4 * M)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    #input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #calc
    A.sort()
    A.reverse()
    sum_A = sum(A)
    if A[M-1] >= sum_A/(4*M):
        print('Yes')
    else:
        print('No')
    #output
