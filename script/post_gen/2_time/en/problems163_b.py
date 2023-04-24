Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) > N:
        print(-1)
    else:
        print(N - sum(A))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) > n:
        print(-1)
    else:
        print(n - sum(a))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N < sum(A):
        print(-1)
    else:
        print(N - sum(A))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    if N < total:
        print(-1)
    else:
        print(N - total)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) > N:
        print(-1)
    else:
        print(N - sum(A))
main()

The second solution is the same as the first, but is written in a more compact way.

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        N -= A[i]
        if N < 0:
            print(-1)
            return
    print(N)

=======
Suggestion 7

def main():
    #Read input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    #Calculate the total number of days of assignments
    total = 0
    for a in A:
        total += a
    
    #If the total number of days of assignments is greater than the number of days of vacation, print -1
    if total > N:
        print(-1)
    else:
        #Otherwise, print the number of days of vacation minus the total number of days of assignments
        print(N - total)
