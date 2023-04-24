Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            sum += i*100 + j
    print(sum)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            ans += i*100 + j
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            ans += 100*i + j
    print(ans)

=======
Suggestion 4

def main():
    # input
    N, K = map(int, input().split())

    # compute
    ans = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            ans += 100*i + j

    # output
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    #print(N, K)
    sum = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            sum += i*100 + j
    print(sum)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    print(N * K * 100 + N * K * 10 + N * K)

=======
Suggestion 7

def main():
    #write code here
    N,K = map(int,input().split())
    sum = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            sum += int(str(i) + '0' + str(j))
    print(sum)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    print(N * 100 * K + N * K)

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    print(N*100+K*10+K)

=======
Suggestion 10

def main():
    n,k=map(int,input().split())
    print((n*100+k)*n+k)

main()
