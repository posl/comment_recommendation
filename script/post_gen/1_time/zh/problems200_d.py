Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    print('No')

=======
Suggestion 2

def solve():
    print 'Yes'
    print '1 1'
    print '1 2'
    return 0

=======
Suggestion 3

def find_subset(N, A):
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] + A[j]) % 200 == 0:
                return True
    return False

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    a = [i % 200 for i in a]
    d = {}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if a[i] == a[j]:
                print('Yes')
                print(1, i)
                print(1, j)
                return
            if a[i] in d:
                d[a[i]].append(i)
            else:
                d[a[i]] = [i]
    for k, v in d.items():
        if len(v) >= 2:
            print('Yes')
            print(len(v), v[0], v[1])
            print(len(v), v[2], v[3])
            return
    print('No')

=======
Suggestion 5

def find_sum_200(A, x, y):
    sum_x = sum([A[i] for i in x])
    sum_y = sum([A[i] for i in y])
    if sum_x % 200 == sum_y % 200 == 0:
        return 0
    else:
        return 1

=======
Suggestion 6

def main():
    print("Hello World")
    return 0

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    a = [sum(a[:i]) % 200 for i in range(1, n + 1)]

    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]

    for k, v in d.items():
        if len(v) >= 2:
            print('Yes')
            print(1, v[0] + 1)
            print(1, v[1] + 1)
            return
    for k, v in d.items():
        if len(v) >= 3:
            print('Yes')
            print(1, v[0] + 1)
            print(2, v[1] + 1, v[2] + 1)
            return
    print('No')

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i] % 200 for i in range(n)]
    dp = [[-1 for _ in range(200)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(200):
            if dp[i][j] == -1:
                continue
            dp[i+1][j] = dp[i][j]
            dp[i+1][(j+a[i])%200] = i
    if dp[n][0] == 0:
        print("No")
        return
    print("Yes")
    ans = []
    i = n
    j = 0
    while i > 0:
        if dp[i][j] != dp[i-1][j]:
            ans.append(i)
            j = (j-a[i-1])%200
        i -= 1
    print(len(ans), *ans)
    ans = []
    i = n
    j = 0
    while i > 0:
        if dp[i][j] != dp[i-1][j]:
            ans.append(i)
            j = (j-a[i-1])%200
        i -= 1
    print(len(ans), *ans)

solve()

=======
Suggestion 10

def solve():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    # a = [180, 186, 189, 191, 218]
    # n = 5
    d = {}
    for i in range(n):
        for j in range(i+1, n):
            if (a[i]+a[j])%200 not in d:
                d[(a[i]+a[j])%200] = [[i, j]]
            else:
                d[(a[i]+a[j])%200].append([i, j])
    for k, v in d.items():
        if len(v) >= 2:
            print('Yes')
            print(len(v[0]), end=' ')
            for i in v[0]:
                print(i+1, end=' ')
            print()
            print(len(v[1]), end=' ')
            for i in v[1]:
                print(i+1, end=' ')
            print()
            return
    print('No')

solve()
