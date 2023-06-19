Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    print(n*100*k*(k+1)//2)

=======
Suggestion 2

def f(n, k):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            sum = sum + i * 100 + j
    return sum

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum += i*100 + j
    print(sum)

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    ans = 0
    for i in range(N):
        for j in range(K):
            room = (i+1)*100 + (j+1)
            ans += room
    print(ans)

=======
Suggestion 5

def main():
    n,k = map(int, input().split())
    print(100 * n * (n+1) * k // 2)

=======
Suggestion 6

def problems203_b(n,k):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum += i*100+j
    return sum

n,k = map(int,input().split())
print(problems203_b(n,k))

=======
Suggestion 7

def sum_room_number(n,k):
    sum=0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum+=i*100+j
    return sum

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    print((N*K*100+N*(N+1)*K//2))

=======
Suggestion 9

def solve():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            ans += i * 100 + j
    print(ans)
