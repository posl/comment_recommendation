Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) + K * N < M * N:
        print(-1)
    else:
        print(max(0, M * N - sum(A)))

=======
Suggestion 2

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) + K * (N - 1) < M * N:
        print(-1)
        return
    print(max(M * N - sum(A), 0))

=======
Suggestion 3

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if (M*N-sum(A)) > K:
        print(-1)
    elif (M*N-sum(A)) < 0:
        print(0)
    else:
        print(M*N-sum(A))

=======
Suggestion 4

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    goal = N * M
    total = sum(A)
    if total >= goal:
        print(0)
    elif total + K < goal:
        print(-1)
    else:
        print(goal - total)

=======
Suggestion 5

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    goal = N * M
    total = sum(A)
    if total >= goal:
        print(0)
    else:
        required = goal - total
        if required > K:
            print(-1)
        else:
            print(required)

=======
Suggestion 6

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(max(0, N * M - sum(A)))
    if sum(A) >= N * M:
        print(0)
    elif sum(A) < N * M:
        if max(A) <= K:
            print(max(A))
        else:
            print(-1)

=======
Suggestion 7

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = sum(A)
    if (N * M) - sumA <= 0:
        print(0)
    elif (N * M) - sumA <= K:
        print((N * M) - sumA)
    else:
        print(-1)

=======
Suggestion 8

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))

    ans = M*N - sum(A)
    if ans <= K and ans >= 0:
        print(ans)
    else:
        print(-1)

=======
Suggestion 9

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    s = sum(A)
    if s >= M*N:
        print(0)
        exit()
    if s + K < M*N:
        print(-1)
        exit()
    print(M*N - s)

=======
Suggestion 10

def main():
    # read input
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))

    # compute sum of A
    A_sum = sum(A)

    # compute required score
    required_score = N * M - A_sum

    # check if required_score is achievable
    if required_score > K:
        print(-1)
    elif required_score > 0:
        print(required_score)
    else:
        print(0)
