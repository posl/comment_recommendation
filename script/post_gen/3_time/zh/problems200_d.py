Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = li

=======
Suggestion 2

def find_seq(n, A):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if (A[i] + A[j]) % 200 == 0:
                return [i + 1], [j + 1]
    return [], []

=======
Suggestion 3

def solve():
    print('No')

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def check(a, b):
    if a == 0 and b == 0:
        return True
    if a == 0 or b == 0:
        return False
    if a == b:
        return False
    if a == 1 and b == 1:
        return False
    return True

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    mod_A = [a % 200 for a in A]
    mod_A.sort()
    for i in range(N):
        if i == N - 1 or mod_A[i] != mod_A[i + 1]:
            continue
        elif i == N - 2 or mod_A[i] != mod_A[i + 2]:
            continue
        else:
            print("Yes")
            print(1, i + 1)
            print(1, i + 2)
            return
    if sum_A % 200 == 0:
        print("Yes")
        print(1, 1)
        print(1, 2)
    else:
        print("No")

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] = a[i] % 200
    dp = [[0 for i in range(200)] for i in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(200):
            if dp[i-1][j] == 1:
                dp[i][j] = 1
                dp[i][(j+a[i-1])%200] = 1
    #print(dp)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if dp[i][0] == 1 and dp[j][0] == 1:
                print("Yes")
                print(i, end=" ")
                for k in range(i):
                    if dp[k+1][0] == 1:
                        print(k+1, end=" ")
                print()
                print(j-i, end=" ")
                for k in range(i, j):
                    if dp[k+1][0] == 1:
                        print(k+1, end=" ")
                print()
                return
    print("No")

main()

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    if N == 2:
        print('Yes')
        print('1 1')
        print('1 2')
        return

    # 用来存储所有可能的和
    s = set()
    # 用来存储和对应的下标
    d = dict()
    for i in range(N):
        for j in range(i+1, N):
            sum = A[i] + A[j]
            if sum % 200 in s:
                print('Yes')
                print('1', end=' ')
                print(d[sum % 200][0] + 1)
                print('1', end=' ')
                print(d[sum % 200][1] + 1)
                print(i + 1, j + 1)
                return
            else:
                s.add(sum % 200)
                d[sum % 200] = (i, j)
    print('No')
