Synthesizing 10/10 solutions

=======
Suggestion 1

def problem203_b():
    n, k = map(int, input().split())
    sum = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            sum += i*100 + j
    print(sum)

=======
Suggestion 2

def calcSum(n,k):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum += int(str(i) + '0' + str(j))
    return sum

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    print((n * (n + 1) * k * (k + 1)) // 4)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    print((n * k * (n + 1) * (k + 1)) // 4)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    print(int((N * (N + 1) * K * (K + 1)) / 4))

=======
Suggestion 6

def solve():
    n, k = map(int, input().split())
    print((n * (n + 1) * k * (k + 1)) // 4)

=======
Suggestion 7

def calc_sum(n, k):
    total_sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            total_sum += int(str(i) + str(j) + str(0))
    return total_sum

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    print(N * (N + 1) * K * 100 // 2)

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    print((n*(n+1)*100*k//2)+(k*(k+1)*100*n//2))

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    print(100*N*(N+1)//2*K)
    return 0
