Synthesizing 10/10 solutions

=======
Suggestion 1

def read_ints():
    return list(map(int, input().split()))

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    # print(a)
    # print(b)
    # print(max(a))
    # print(min(a))
    # print(max(b))
    # print(min(b))
    # print(range(1, 11))
    # print(range(2, 12))
    # print(range(3, 13))
    # print(range(4, 14))
    # print(range(5, 15))
    # print(range(6, 16))
    # print(range(7, 17))
    # print(range(8, 18))
    # print(range(9, 19))
    # print(range(10, 20))
    # print(range(11, 21))
    # print(range(12, 22))
    # print(range(13, 23))
    # print(range(14, 24))
    # print(range(15, 25))
    # print(range(16, 26))
    # print(range(17, 27))
    # print(range(18, 28))
    # print(range(19, 29))
    # print(range(20, 30))
    # print(range(21, 31))
    # print(range(22, 32))
    # print(range(23, 33))
    # print(range(24, 34))
    # print(range(25, 35))
    # print(range(26, 36))
    # print(range(27, 37))
    # print(range(28, 38))
    # print(range(29, 39))
    # print(range(30, 40))
    # print(range(31, 41))
    # print(range(32, 42))
    # print(range(33, 43))
    # print(range(34, 44))
    # print(range(35, 45))
    # print(range(36, 46))
    # print(range(37, 47))
    # print(range(38, 48))
    # print(range(39, 49))
    # print(range(40, 50))
    # print(range(41, 51))
    # print(range(42,

=======
Suggestion 3

def check_login_days(n, login_days):
    login_days.sort()
    days = [0] * n
    for i in range(n):
        for j in range(i, n):
            if login_days[i] <= login_days[j] < login_days[i] + n:
                days[j - i] += 1
            else:
                break
    return days

=======
Suggestion 4

def solve():
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    #print(len(A))
    #print(len(B))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    #print(len(A[1:]))
    #print(len(B[:-1]))
    #print(A[1:])
    #print(B[:-1])
    #print(len(A[1:]) == len(B[:-1]))
    C = [0]*N
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i] <= A[j] and A[j] < A[i]+B[i]:
                    C[i] += 1
    print(C)
    for i in range(N):
        print(C[i],

=======
Suggestion 5

def main():
    n = int(input())
    d = [0] * (10**9 + 1)
    for _ in range(n):
        a, b = map(int, input().split())
        d[a] += 1
        d[a+b] -= 1
    for i in range(10**9):
        d[i+1] += d[i]
    print(*d[1:])

=======
Suggestion 6

def main():
    N = int(input())
    login = [0] * (10**9 + 2)
    for i in range(N):
        A, B = map(int, input().split())
        login[A] += 1
        login[A + B] -= 1
    for i in range(10**9 + 1):
        login[i + 1] += login[i]
    for i in range(1, N + 1):
        ans = 0
        for j in range(10**9 + 1):
            if login[j] == i:
                ans += 1
        print(ans)

=======
Suggestion 7

def solve(n,ab):
    ab.sort(key=lambda x:x[0])
    ans = [0]*n
    for i in range(n):
        a,b = ab[i]
        ans[b-1] += 1
    for i in range(n-2,-1,-1):
        ans[i] += ans[i+1]
    return ans

=======
Suggestion 8

def main():
    # 读入数据
    N = int(input())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append((A, B))

    # 计算答案
    D = [0] * (N + 1)
    for i in range(N):
        A, B = AB[i]
        D[A] += 1
        D[A + B] -= 1

    for i in range(N):
        D[i + 1] += D[i]

    # 输出答案
    print(*D[1:])

=======
Suggestion 9

def main():
    N = int(input())
    #print(N)
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    dict = {}
    for i in range(N):
        for j in range(B[i]):
            if A[i]+j in dict:
                dict[A[i]+j] += 1
            else:
                dict[A[i]+j] = 1
    #print(dict)
    for i in range(N):
        if i == N-1:
            print(dict[i+1])
        else:
            print(dict[i+1], end=" ")

=======
Suggestion 10

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A, B)

    # D = [0] * N
    # for i in range(N):
    #     for j in range(A[i], A[i]+B[i]):
    #         D[j-1] += 1
    # print(D)

    # D = [0] * (10**9 + 1)
    # for i in range(N):
    #     for j in range(A[i], A[i]+B[i]):
    #         D[j] += 1
    # print(D)

    # D = [0] * (10**9 + 1)
    # for i in range(N):
    #     D[A[i]] += 1
    #     D[A[i]+B[i]] -= 1
    # print(D)

    # D = [0] * (10**9 + 1)
    # for i in range(N):
    #     D[A[i]] += 1
    #     D[A[i]+B[i]] -= 1
    # for i in range(1, 10**9+1):
    #     D[i] += D[i-1]
    # print(D)

    D = [0] * (10**9 + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i]+B[i]] -= 1
    for i in range(1, 10**9+1):
        D[i] += D[i-1]
    print(*D[1:])
