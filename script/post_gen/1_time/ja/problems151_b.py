Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N * M <= sum(A):
        print(0)
    elif N * M - sum(A) <= K:
        print(N * M - sum(A))
    else:
        print(-1)

=======
Suggestion 2

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M * N - sum(A) <= K:
        print(max(0, M * N - sum(A)))
    else:
        print(-1)

=======
Suggestion 3

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if (N * M) - sum(A) > K:
        print(-1)
    elif (N * M) - sum(A) < 0:
        print(0)
    else:
        print((N * M) - sum(A))

=======
Suggestion 4

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    if M * N - sum_A > K:
        print(-1)
    else:
        print(max(M * N - sum_A, 0))

=======
Suggestion 5

def main():
    n,k,m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = n*m - sum(a)
    if ans < 0:
        ans = 0
    elif ans > k:
        ans = -1
    print(ans)

=======
Suggestion 6

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    x = n * m - s
    if x <= k:
        if x < 0:
            print(0)
        else:
            print(x)
    else:
        print(-1)

=======
Suggestion 7

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    if total >= N * M:
        print(0)
    elif total + K < N * M:
        print(-1)
    else:
        print(N * M - total)

=======
Suggestion 8

def main():
    N,K,M = map(int,input().split())
    A = list(map(int,input().split()))

    if N*M <= sum(A):
        print(0)
    elif N*M - K <= sum(A):
        print(N*M - sum(A))
    else:
        print(-1)

=======
Suggestion 9

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    x = n*m-sum(a)
    print(x if x > 0 else 0 if x <= 0 else -1)

=======
Suggestion 10

def is_achieved_goal(score_list, score, goal):
    score_list.append(score)
    score_list.sort()
    score_list.reverse()
    score_list.pop()
    score_list.reverse()
    if sum(score_list) / len(score_list) >= goal:
        return True
    else:
        return False
