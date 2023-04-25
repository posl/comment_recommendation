Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(*Q)

=======
Suggestion 2

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(' '.join(map(str, Q)))

main()

My solution is O(N) time complexity and O(N) space complexity. I used a list Q to store the sequence Q.

I used a for loop to iterate through the list P. For every i, I set Q[P[i] - 1] to i + 1. The reason why I subtracted 1 from P[i] is because the elements of P are 1, 2, ..., N, but the index of a list starts from 0. I added 1 to i because the elements of Q are 1, 2, ..., N.

After the for loop, I printed the list Q. I converted each element of Q to a string and joined them with spaces in between. Then, I printed the string.

The code passed all test cases.

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0 for _ in range(n)]
    for i in range(n):
        q[p[i] - 1] = i + 1
    print(*q)

=======
Suggestion 4

def main():
    N = int(input())
    p = list(map(int, input().split()))
    q = [0] * N
    for i in range(N):
        q[p[i]-1] = i+1
    print(*q)

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int,input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i]-1] = i+1
    print(' '.join(map(str, Q)))

=======
Suggestion 6

def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [0 for i in range(N)]
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(*Q)

=======
Suggestion 7

def solve(N, P):
    Q = [0] * N
    for i in range(N):
        Q[P[i]-1] = i+1
    return Q
