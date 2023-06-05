Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            ans += int(str(i) + '0' + str(j))
    print(ans)

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    print( (N*(N+1)*K//2)*100 + (K*(K+1)*N//2) )

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
    n,k = map(int,input().split())
    print((n*(n+1)*100*k//2)+(k*(k+1)*n//2))

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    print(100*N*(N+1)//2*K)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            sum += i*100 + j

    print(sum)

=======
Suggestion 7

def sum_room_number(n,k):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum += (i*100+j)
    return sum

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    print((100 * n + 10 * k + 3) * n * k // 2)
