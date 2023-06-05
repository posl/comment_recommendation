Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        a[i] = max(0, a[i] - b[i])
        b[i] = max(0, b[i] - a[i])
        ans += min(a[i + 1], b[i])
        a[i + 1] = max(0, a[i + 1] - b[i])
        b[i] = max(0, b[i] - a[i + 1])
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] >= b[i]:
            ans += b[i]
            a[i] -= b[i]
            b[i] = 0
        else:
            ans += a[i]
            b[i] -= a[i]
            a[i] = 0
        if a[i + 1] >= b[i]:
            ans += b[i]
            a[i + 1] -= b[i]
            b[i] = 0
        else:
            ans += a[i + 1]
            b[i] -= a[i + 1]
            a[i + 1] = 0
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] <= B[i]:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
        else:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        if A[i+1] <= B[i]:
            ans += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
        else:
            ans += B[i]
            A[i+1] -= B[i]
            B[i] = 0
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] <= B[i]:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
        else:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        if A[i+1] <= B[i]:
            ans += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
        else:
            ans += B[i]
            A[i+1] -= B[i]
            B[i] = 0
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] <= B[i]:
            ans += A[i]
            B[i] -= A[i]
            if A[i+1] <= B[i]:
                ans += A[i+1]
                A[i+1] = 0
            else:
                ans += B[i]
                A[i+1] -= B[i]
        else:
            ans += B[i]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        if a_list[i] > b_list[i]:
            sum += b_list[i]
            a_list[i] -= b_list[i]
            b_list[i] = 0
        else:
            sum += a_list[i]
            b_list[i] -= a_list[i]
            a_list[i] = 0
        if a_list[i + 1] > b_list[i]:
            sum += b_list[i]
            a_list[i + 1] -= b_list[i]
            b_list[i] = 0
        else:
            sum += a_list[i + 1]
            b_list[i] -= a_list[i + 1]
            a_list[i + 1] = 0

    print(sum)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # print(N, A, B)

    ans = 0
    for i in range(N):
        if A[i] <= B[i]:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
        else:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        if A[i+1] <= B[i]:
            ans += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
        else:
            ans += B[i]
            A[i+1] -= B[i]
            B[i] = 0
    print(ans)

=======
Suggestion 8

def max_monster(N,A,B):
    max_monster = 0
    for i in range(N):
        if B[i] >= A[i]:
            max_monster += A[i]
            B[i] = B[i] - A[i]
            A[i] = 0
        else:
            max_monster += B[i]
            A[i] = A[i] - B[i]
            B[i] = 0
        if B[i] >= A[i+1]:
            max_monster += A[i+1]
            B[i] = B[i] - A[i+1]
            A[i+1] = 0
        else:
            max_monster += B[i]
            A[i+1] = A[i+1] - B[i]
            B[i] = 0
    return max_monster

=======
Suggestion 9

def solve(n, a, b):
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        a[i] -= min(a[i], b[i])
        b[i] -= min(a[i], b[i])
        ans += min(a[i+1], b[i])
        a[i+1] -= min(a[i+1], b[i])
        b[i] -= min(a[i+1], b[i])
    return ans

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        if A[i] >= B[i]:
            cnt += B[i]
            A[i] -= B[i]
            B[i] = 0
        else:
            cnt += A[i]
            B[i] -= A[i]
            A[i] = 0
            if A[i+1] >= B[i]:
                cnt += B[i]
                A[i+1] -= B[i]
                B[i] = 0
            else:
                cnt += A[i+1]
                B[i] -= A[i+1]
                A[i+1] = 0
    print(cnt)
