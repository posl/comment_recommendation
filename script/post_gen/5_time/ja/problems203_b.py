Synthesizing 10/10 solutions

=======
Suggestion 1

def calc(n, k):
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            ans += i * 100 + j
    return ans

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    room_num = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            room_num += 100*i + j
    print(room_num)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            sum += i * 100 + j
    print(sum)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            ans += int(str(i) + '0' + str(j))
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            ans += int(str(i) + '0' + str(j))
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(n):
        for j in range(k):
            ans += (i+1)*100 + (j+1)
    print(ans)

main()

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    print(sum([int(str(i) + str(j)) for i in range(1, n+1) for j in range(1, k+1)]))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            ans += i*100 + j
    print(ans)
main()

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            ans += i*100 + j
    print(ans)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum += i*100+j
    print(sum)
