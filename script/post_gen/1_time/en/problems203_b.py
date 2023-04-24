Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            sum += i*100+j
    print(sum)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            ans += int(str(i) + '0' + str(j))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    print((N*100 + N*10 + N) + (K*100 + K*10 + K))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    print((N * 100 + K) * (N * K) // 2)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    print((N * 100 + K) * (N * 100 + K))

main()

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    print(N * 100 + K * 10 + N + K)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    print(100*N + 10*K + N + K)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    print((N*100+K)*N)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    print(100 * N * K)
