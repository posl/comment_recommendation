Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    for i in a:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    total = 0
    for i in cnt:
        total += cnt[i] * (cnt[i] - 1) // 2
    for i in a:
        print(total - (cnt[i] - 1))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(1, n + 1):
        ans += b[i] * (b[i] - 1) // 2
    for i in range(n):
        print(ans - (b[a[i]] - 1))

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[A[i]-1] += 1
    for i in range(N):
        print(ans[i])
    return 0

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = {}
    for i in range(n):
        c[a[i]] = c.get(a[i], 0) + 1
    ans = [0 for i in range(n)]
    for i in range(n):
        ans[i] = c[a[i]] * (c[a[i]] - 1) // 2
    total = sum(ans)
    for i in range(n):
        print(total - ans[a[i]] + 1)

=======
Suggestion 5

def solve():
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0
    for i in range(n):
        ans += c[a[i]] - 1
    for i in range(n):
        print(ans - c[a[i]] + 1)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for a in A:
        B[a] += 1
    ans = (N * (N - 1)) // 2
    for b in B[1:]:
        ans -= (b * (b - 1)) // 2
    for a in A:
        print(ans + B[a] - 1)

=======
Suggestion 7

def solve(N, A):
    from collections import defaultdict
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    s = 0
    for a in A:
        s += d[a] - 1
    return s

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A + [0]
    #print(A)
    cnt = {}
    for i in range(1, N+1):
        if A[i] in cnt:
            cnt[A[i]] += 1
        else:
            cnt[A[i]] = 1
    #print(cnt)
    ans = 0
    for i in range(1, N+1):
        ans += cnt[A[i]] - 1
    for i in range(1, N+1):
        print(ans - cnt[A[i]] + 1)

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = 0
    count = 0
    pre = -1
    for i in range(N + 1):
        if pre == A[i]:
            count += 1
        else:
            ans += count * (count - 1) // 2
            count = 1
            pre = A[i]
    for i in range(N):
        print(ans - (A.index(A[i]) - i) + (N - A.index(A[i]) - 1))
solve()

=======
Suggestion 10

def main():
    # Get the number of balls
    num_balls = int(input())
    # Get the numbers on the balls
    ball_numbers = list(map(int, input().split()))
    # Create a dictionary to store the number of appearances of each ball number
    ball_dict = {}
    for ball_number in ball_numbers:
        if ball_number in ball_dict:
            ball_dict[ball_number] += 1
        else:
            ball_dict[ball_number] = 1
    # Calculate the total number of ways to choose two distinct balls (disregarding order) from the N-1 balls other than the k-th ball so that the integers written on them are equal
    total_ways = 0
    for ball_number in ball_dict:
        total_ways += ball_dict[ball_number] * (ball_dict[ball_number] - 1) // 2
    # Print the number of ways to choose two distinct balls (disregarding order) from the N-1 balls other than the k-th ball so that the integers written on them are equal
    for ball_number in ball_numbers:
        print(total_ways - (ball_dict[ball_number] - 1))
