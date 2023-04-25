Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            ans += i*100 + j
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    print(100 * N * K + 100 * N + 100 * K + N * K)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    print(N * 100 + K)

main()

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    print((N*100+K)*N+K)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    print(n * 100 + k)

=======
Suggestion 6

def main():
    # Get N and K
    N, K = map(int, input().split())
    # Calculate the sum of the room numbers
    sum = 0
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            sum += 100 * i + j
    # Print the answer
    print(sum)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    print((N*100 + K)*N)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    print((n*100+k)*n+k)

=======
Suggestion 9

def sum_room_number():
    N, K = map(int, input().split())
    print(N * 100 * K + K * (K + 1) // 2)

sum_room_number()
