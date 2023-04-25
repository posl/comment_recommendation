Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a[::-1]
    ans = 0
    for i in range(n-1):
        if a[i] <= a[i+1]:
            continue
        else:
            ans += a[i] - a[i+1]
            a[i+1] = a[i]
    print(ans)
main()

The first line of the input is the number of persons N. The second line is the heights of the persons A_1, A_2, ..., A_N. We want to have each person stand on a stool of some heights - at least zero - so that the following condition is satisfied for every person:

Condition: Nobody in front of the person is taller than the person. Here, the height of a person includes the stool.

Find the minimum total height of the stools needed to meet this goal.

We can see that the problem is equivalent to the following. For each person, we want to have the person stand on a stool of height at least the height of the tallest person in front of the person. So, we want to have the person stand on a stool of height at least the maximum height of the persons in front of the person. We can see that the answer is the sum of the differences between the heights of the persons and the heights of the stools.

So, we can solve the problem by going through the persons in reverse order. When we want to have the i-th person stand on a stool of height at least a_i, we can see that the i-th person can stand on a stool of height at least a_i if and only if the i-th person is taller than the i+1-th person. If the i-th person is not taller than the i+1-th person, we can see that the i-th person can stand on a stool of height at least a_i if and only if the i+1-th person stands on a stool of height at least a_i - (a_i - a_{i+1}). So, we can see that we can make the i-th person stand on a stool of height at least a_i if and only if the i+1-th person stands on a stool of height at least a_i. If the i-th person is taller than the i+1-th person, we can see that the i-th person can stand on a stool of height at least a_i

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += a[i] - 1
        else:
            if a[i] > a[i - 1]:
                ans += a[i] - a[i - 1] - 1
            elif a[i] == a[i - 1]:
                ans += a[i] - 1
            else:
                ans += a[i] - 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A[::-1]
    ans = 0
    for i in range(1, N):
        if A[i] <= A[i - 1]:
            ans += A[i - 1] - A[i] + 1
            A[i] = A[i - 1] + 1
    print(ans)

=======
Suggestion 4

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] > i:
            ans += A[i] - i
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1, -1, -1):
        if A[i] > ans:
            ans += A[i] - ans - 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] - 1 - i
    print(ans)

=======
Suggestion 7

def  main():
    N =  int (input())
    A = [ int (a)  for  a  in  input().split()]
    A = [0] + A + [0]
    ans = 0 
    for  i  in  range(1, N + 2):
        ans +=  max (A[i - 1], A[i])
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(0)
        return
    A.sort()
    A = A[::-1]
    B = [A[0]]
    for i in range(1, N):
        if A[i] < B[-1]:
            B.append(A[i])
        else:
            B.append(B[-1])
    print(sum(A) - sum(B))
    return

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # DP[i] = i番目の人が立てる最小のスツールの高さ
    DP = [0] * N

    for i in range(N):
        if i == 0:
            DP[i] = 0
        elif i == 1:
            DP[i] = max(0, A[i - 1] - A[i])
        else:
            DP[i] = max(0, A[i - 1] - A[i] + DP[i - 2])

    print(sum(DP))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # dp[i][j] := i番目の人がjの高さのstoolを持つときの、stoolの合計高さの最小値
    # 0 <= j <= A[i]
    dp = [[float('inf')] * (max(A) + 1) for _ in range(N)]
    dp[0][0] = 0
    dp[0][A[0]] = A[0]
    for i in range(1, N):
        for j in range(max(A) + 1):
            if j < A[i]:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][A[i]] + j)
            else:
                dp[i][j] = dp[i - 1][j]

    print(min(dp[-1]))
