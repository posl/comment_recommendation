Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, x + 1):
        if x % i == 0:
            for j in range(n):
                for k in range(l[j][0]):
                    if l[j][k + 1] == i:
                        ans += 1
                        break
    print(ans)

=======
Suggestion 3

def get_divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split()))[1:])
    #print(l)
    #print(n, x)
    #print(l)
    #print(l[0])
    #print(l[0][0])
    #print(l[0][1])
    #print(l[0][2])
    #print(l[1])
    #print(l[1][0])
    #print(l[1][1])
    #print(l[1][2])
    #print(l[2])
    #print(l[2][0])
    #print(l[2][1])
    #print(l[2][2])
    res = 0
    for i in range(n):
        for j in range(len(l[i])):
            if x % l[i][j] == 0:
                res += 1
    print(res)

=======
Suggestion 5

def main():
    N,X = map(int,input().split())
    L = []
    for i in range(N):
        L.append(list(map(int,input().split())))
    print(L)
    print(N)
    print(X)

=======
Suggestion 6

def get_input():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    return N, X, L

=======
Suggestion 7

def get_divisors(n):
    # 約数を列挙する
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

=======
Suggestion 8

def solve():
    N, X = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    # ここにプログラムを追記
    # print(N, X, A)

    # 1. 全探索
    # 2. 二分探索
    # 3. DP
    # 4. 素因数分解

    # 1. 全探索
    # def dfs(i, x):
    #     if i == N:
    #         return x == X
    #     for j in range(A[i][0]):
    #         if dfs(i + 1, x * A[i][j + 1]):
    #             return True
    #     return False
    # print('Yes' if dfs(0, 1) else 'No')

    # 2. 二分探索
    # def dfs(i, x):
    #     if i == N:
    #         return x == X
    #     for j in range(A[i][0]):
    #         if dfs(i + 1, x * A[i][j + 1]):
    #             return True
    #     return False
    # print('Yes' if dfs(0, 1) else 'No')

    # 3. DP
    # dp = [0] * (X + 1)
    # dp[1] = 1
    # for i in range(N):
    #     for j in range(X, 0, -1):
    #         if dp[j] == 1:
    #             for k in range(A[i][0]):
    #                 dp[j * A[i][k + 1]] = 1
    # print('Yes' if dp[X] else 'No')

    # 4. 素因数分解
    # print(N, X, A)
    # for i in range(N):
    #     print(A[i][0])
    #     for j in range(A[i][0]):
    #         print(A[i][j + 1])
    # print('Yes' if dfs(0, 1) else 'No')

    # 5. 素因数分

=======
Suggestion 9

def main():
    print("hello world!")

=======
Suggestion 10

def main():
    n,x = map(int,input().split())
    bag = []
    for i in range(n):
        bag.append(list(map(int,input().split())))
    print(bag)
    res = 0
    for i in range(n):
        for j in range(len(bag[i])):
            if bag[i][j] == x:
                res += 1
            for k in range(i+1,n):
                if bag[i][j]*bag[k][j] == x:
                    res += 1
    print(res)
