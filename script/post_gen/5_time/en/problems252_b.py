Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(K):
        if B[i] > N:
            continue
        if A[0] == A[B[i]-1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)

    for i in range(K):
        if A[i] > A[B[i]-1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)

    for i in range(K):
        if A[i] > A[B[i]-1]:
            print("Yes")
            return 0

    print("No")
    return 0

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort()

    for i in range(K):
        if A[i] >= B[i]:
            print("No")
            return

    print("Yes")
    return

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print('Yes' if len(set(a) & set(b)) > 0 else 'No')

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    for i in range(K):
        if A[i] == B[i]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_a = max(A)
    max_b = max(B)

    if max_a > max_b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N, K = input().split()
    N = int(N)
    K = int(K)
    A = input().split()
    B = input().split()
    A = [int(s) for s in A]
    B = [int(s) for s in B]
    A.sort(reverse=True)
    B.sort()
    for i in range(K):
        for j in range(N):
            if B[i] == j+1:
                A[j] = 0
    if max(A) == 0:
        print("No")
    else:
        print("Yes")
main()

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    max_A = max(A)
    max_B = max(B)
    if max_A > max_B:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    # Take input from stdin
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    # Sort the list a
    a.sort(reverse=True)

    # Get the max value of b
    max_b = max(b)

    # Get the index of max value of b
    max_b_index = b.index(max_b)

    # Get the max value of a
    max_a = a[0]

    # Check if max value of b is less than max value of a
    if max_b < max_a:
        print("Yes")
    else:
        print("No")
