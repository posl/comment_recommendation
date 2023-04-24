Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum([a[i] * b[i] for i in range(n)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum([a[i] * b[i] for i in range(n)]) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if sum([A[i]*B[i] for i in range(N)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("Yes" if sum([a[i] * b[i] for i in range(n)]) == 0 else "No")

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    if sum([A[i]*B[i] for i in range(N)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print('Yes' if sum([a[i] * b[i] for i in range(n)]) == 0 else 'No')

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    print("Yes" if sum([A[i]*B[i] for i in range(N)]) == 0 else "No")

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    
    if sum([A[i]*B[i] for i in range(N)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    # Read the number of dimensions
    n = int(input())
    # Read the first vector
    a = list(map(int, input().split()))
    # Read the second vector
    b = list(map(int, input().split()))
    # Compute the inner product
    ip = sum([a[i] * b[i] for i in range(n)])
    # Print the result
    print('Yes' if ip == 0 else 'No')
