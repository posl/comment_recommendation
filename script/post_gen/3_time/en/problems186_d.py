Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * i - A[i] * (N - i - 1)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += (i+1)*(A[i+1]-A[i])
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += (N-1-i)*A[i] - i*A[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * i - A[i] * (N - i - 1)
    print(ans)

main()

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A.sort()
    ans = 0
    for i in range(N):
        ans += i * A[i] - (N - i - 1) * A[i]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    S = [0] * N
    S[0] = A[0]
    for i in range(1, N):
        S[i] = S[i - 1] + A[i]
    ans = 0
    for i in range(1, N):
        ans += i * A[i] - S[i - 1]
    print(ans * 2)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += (i+1)*A[i]-(N-i-1)*A[i]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    B = [0]*(N+1)
    for i in range(1,N+1):
        B[i] = B[i-1]+A[i-1]
    ans = 0
    for i in range(N):
        ans += (i+1)*A[i]-B[i]
    print(2*ans)

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    for i in range(N):
        ans += (i + 1) * A[i] - B[i]
    print(ans)
    return

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 1. Sort the array
    A.sort()

    # 2. Calculate the sum of |A_i-A_j| over all pairs i,j such that 1≦ i < j ≦ N
    #    This is done in two steps:
    #    2.1. Calculate the sum of |A_i-A_j| over all pairs i,j such that 1≦ i < j ≦ N/2
    #    2.2. Calculate the sum of |A_i-A_j| over all pairs i,j such that N/2 < i < j ≦ N
    #         and add it to the sum calculated in 2.1
    #    The sum in 2.2 can be calculated by reversing the order of the array
    #    and performing the same calculation as in 2.1
    #    This is done by the function calc_diff
    sum = calc_diff(A[:N//2]) + calc_diff(A[N//2:][::-1])

    # 3. Print the answer
    print(sum)
