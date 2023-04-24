Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i):
            ans += (A[i] - A[j]) ** 2
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i):
            ans += (a[i] - a[j]) ** 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(1, N):
        for j in range(i):
            sum += (A[i] - A[j]) ** 2
    print(sum)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i - 1]) ** 2
    ans *= (N - 1)
    for i in range(1, N - 1):
        ans += (A[i + 1] - A[i - 1]) * (A[i] - A[i - 1]) - (A[i] - A[i - 1]) * (A[i] - A[i - 1])
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    sum = 0
    for i in range(1,N):
        for j in range(i):
            sum += (A[i] - A[j]) ** 2
    print(sum)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = 0
    for i in range(1, N):
        S += (A[i] - A[i-1])**2
    S += A[0]**2 + A[-1]**2
    for i in range(1, N-1):
        print(S - (A[i] - A[i-1])**2 - (A[i+1] - A[i])**2 + (A[i+1] - A[i-1])**2)
    print(S - A[0]**2 - A[-1]**2 + A[-1]**2 + A[0]**2)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    assert len(A) == N
    assert 2 <= N <= 3 * 10 ** 5
    assert all(abs(x) <= 200 for x in A)
    print(sum((A[i] - A[j]) ** 2 for i in range(1, N) for j in range(i)))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    sum_A2 = sum([a ** 2 for a in A])
    ans = 0
    for i in range(N):
        ans += (N - i - 1) * A[i] ** 2 - 2 * A[i] * (sum_A - A[i]) + sum_A2
        sum_A -= A[i]
        sum_A2 -= A[i] ** 2
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    B = [A[0]]
    for i in range(1, N):
        B.append(B[i-1] + A[i])
    ans = 0
    for i in range(1, N):
        ans += A[i] * i - B[i-1]
    print(ans * 2)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)

    # 1. sum_{i = 2}^{N} sum_{j = 1}^{i - 1} (A_i - A_j)^2
    # 2. sum_{i = 2}^{N} sum_{j = 1}^{i - 1} (A_i^2 - 2A_iA_j + A_j^2)
    # 3. sum_{i = 2}^{N} sum_{j = 1}^{i - 1} (A_i^2 - 2A_iA_j + A_j^2) = sum_{i = 2}^{N} A_i^2 - 2sum_{i = 2}^{N} A_iA_j + sum_{i = 2}^{N} sum_{j = 1}^{i - 1} A_j^2
    # 4. sum_{i = 2}^{N} A_i^2 - 2sum_{i = 2}^{N} A_iA_j + sum_{i = 2}^{N} sum_{j = 1}^{i - 1} A_j^2 = sum_{i = 2}^{N} A_i^2 - 2sum_{i = 2}^{N} A_iA_j + sum_{i = 2}^{N} sum_{j = 1}^{i - 1} A_j^2 = sum_{i = 2}^{N} A_i^2 - 2sum_{i = 2}^{N} A_iA_j + sum_{i = 2}^{N} sum_{j = 1}^{i - 1} A_j^2 = sum_{i = 2}^{N} A_i^2 - 2sum_{i = 2}^{N} A_iA_j + sum_{i = 2}^{N} sum_{j = 1}^{i - 1} A_j^2 = sum_{i = 2}^{N} A_i^2 - 2sum_{i = 2}^{N} A_iA_j + sum_{i =
