Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 200
    b = [[] for _ in range(mod)]
    c = [[] for _ in range(mod)]
    for i in range(1, 1 << n):
        s = 0
        for j in range(n):
            if i >> j & 1:
                s += a[j]
                s %= mod
        if len(b[s]) == 0:
            b[s] = [j + 1 for j in range(n) if i >> j & 1]
        else:
            c[s] = [j + 1 for j in range(n) if i >> j & 1]
            break
    if len(c[s]) == 0:
        print("No")
    else:
        print("Yes")
        print(len(b[s]), *b[s])
        print(len(c[s]), *c[s])

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    dp = [[0]*(200) for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(200):
            dp[i][j] = dp[i-1][j]
        dp[i][A[i]%200] = 1
        for j in range(200):
            dp[i][(j+A[i])%200] |= dp[i-1][j]
    for i in range(200):
        if dp[N][i] and dp[N][(i+1)%200]:
            B = []
            C = []
            for j in range(N, 0, -1):
                if dp[j-1][i]:
                    B.append(j)
                    i = (i-A[j])%200
                elif dp[j-1][(i+200-A[j])%200]:
                    C.append(j)
                    i = (i-A[j]+200)%200
            print('Yes')
            print(len(B), ' '.join(map(str, B)))
            print(len(C), ' '.join(map(str, C)))
            return
    print('No')
solve()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    A_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        A_sum[i] = A_sum[i - 1] + A[i]
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if x == y:
                continue
            B = [0] * (x + 1)
            C = [0] * (y + 1)
            for i in range(1, x + 1):
                B[i] = i
            for i in range(1, y + 1):
                C[i] = i
            flag = False
            for i in range(1, x + 1):
                for j in range(1, y + 1):
                    if B[i] == C[j]:
                        flag = True
                        break
                if flag:
                    break
            if flag:
                continue
            if (A_sum[B[x]] - A_sum[B[0]]) % 200 == (A_sum[C[y]] - A_sum[C[0]]) % 200:
                print("Yes")
                print(x, end=" ")
                for i in range(1, x + 1):
                    print(B[i], end=" ")
                print()
                print(y, end=" ")
                for i in range(1, y + 1):
                    print(C[i], end=" ")
                print()
                return
    print("No")
    return

=======
Suggestion 5

def check(s, a):
    if len(s) == 0:
        return True
    if len(s) == 1 and s[0] == a:
        return False
    for i in range(1, len(s)):
        if s[i] == a:
            return False
    return True

=======
Suggestion 6

def solution():
    pass

=======
Suggestion 7

def getSum(list):
    sum = 0
    for i in list:
        sum += i
    return sum

=======
Suggestion 8

def find_seq(nums, mod):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i] + nums[j]) % mod == 0:
                return (i,j)
    return None

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = []
    C = []
    for i in range(N):
        if A[i]%200 == 0:
            B.append(i+1)
        elif A[i]%200 == 100:
            C.append(i+1)
    if len(B) == 0 and len(C) == 0:
        print("No")
    elif len(B) == 0 and len(C) != 0:
        print("Yes")
        print("1",C[0])
        print("1",C[1])
    elif len(B) != 0 and len(C) == 0:
        print("Yes")
        print("1",B[0])
        print("1",B[1])
    else:
        print("Yes")
        print("1",B[0])
        print("1",C[0])
solve()
