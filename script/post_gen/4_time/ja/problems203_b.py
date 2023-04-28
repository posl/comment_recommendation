Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            ans += i * 100 + j
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            ans += int(str(i) + '0' + str(j))
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            ans += i*100 + j
    print(ans)

=======
Suggestion 4

def solve():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            ans += int(str(i) + str(0) + str(j))
    print(ans)

=======
Suggestion 5

def main():
    n,k = map(int, input().split())
    ans = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            ans += i*100 + j
    print(ans)
main()

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(n):
        for j in range(k):
            ans += (i+1)*100 + (j+1)
    print(ans)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    #print(n, k)
    total = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            total += i*100 + j
    print(total)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    print((n * (n + 1) * k * 100 + (n * k * (k + 1)) // 2))
