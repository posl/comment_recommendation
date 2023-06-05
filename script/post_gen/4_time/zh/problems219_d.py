Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f():
    N = int(input())
    X,Y = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = float('inf')
    for i in range(N):
        for j in range(N):
            if A[i]+B[j]>=X and A[i]+B[j]>=Y:
                ans = min(ans,i+j+2)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

=======
Suggestion 2

def main():
    # 读取输入
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    # 处理
    # 1. 如果x，y都大于a，b的和，那么肯定是-1
    if x > sum(a) or y > sum(b):
        print(-1)
        return
    # 2. 如果x，y都小于a，b的最小值，那么肯定是-1
    if x < min(a) or y < min(b):
        print(-1)
        return
    # 3. 如果x，y都等于a，b的最小值，那么肯定是1
    if x == min(a) and y == min(b):
        print(1)
        return
    # 4. 如果x，y都等于a，b的和，那么肯定是n
    if x == sum(a) and y == sum(b):
        print(n)
        return
    # 5. 如果x，y都等于a，b的最大值，那么肯定是n
    if x == max(a) and y == max(b):
        print(n)
        return
    # 6. 如果x，y都等于a，b的最大值，那么肯定是n
    if x == max(a) and y == max(b):
        print(n)
        return
    # 7. 如果x，y都等于a，b的最大值，那么肯定是n
    if x == max(a) and y == max(b):
        print(n)
        return
    # 8. 如果x，y都等于a，b的最大值，那么肯定是n
    if x == max(a) and y == max(b):
        print(n)
        return
    # 9. 如果x，y都等于a，b的最大值，那么肯定是n
    if x ==

=======
Suggestion 3

def solve():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[0 for i in range(300 * 300 + 1)] for i in range(300 + 1)] for i in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(300):
            for k in range(300 * 300 + 1):
                if dp[i][j][k] == 1:
                    dp[i + 1][j][k] = 1
                    if j + 1 <= 300:
                        dp[i + 1][j + 1][k + A[i]] = 1
    ans = -1
    for i in range(300 * 300 + 1):
        if dp[N][X][i] == 1 and dp[N][Y][i] == 1:
            ans = i
            break
    print(ans)
solve()

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #print(a)
    #print(b)
    #print(x)
    #print(y)
    #print(n)
    #print(len(a))
    #print(len(b))
    #print(len(a) == len(b))
    #print(len(a) == n)
    #print(len(b) == n)
    #print(len(a) == len(b) == n)
    #print(len(a) == len(b) == n == True)
    #print(len(a) == len(b) == n == True == True)
    #print(len(a) == len(b) == n == True == True == True)
    #print(len(a) == len(b) == n == True == True == True == True)
    #print(len(a) == len(b) == n == True == True == True == True == True)
    #print(len(a) == len(b) == n == True == True == True == True == True == True)
    #print(len(a) == len(b) == n == True == True == True == True == True == True == True)
    #print(len(a) == len(b) == n == True == True == True == True == True == True == True == True)
    #print(len(a) == len(b) == n == True == True == True == True == True == True == True == True == True)
    #print(len(a) == len(b) == n == True == True == True == True == True == True == True == True == True == True)
    #print(len(a) == len(b) == n == True == True == True == True == True == True == True == True == True == True == True)
    #print(len(a) == len(b) == n == True == True == True == True == True == True == True == True == True == True == True == True)
    #print(len(a) == len(b) == n == True == True == True == True == True == True == True == True == True == True == True == True == True)
    #print(len(a) == len(b) == n ==

=======
Suggestion 6

def solve():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False for _ in range(Y+1)] for _ in range(X+1)]
    dp[0][0] = True
    for i in range(N):
        for x in range(X, -1, -1):
            for y in range(Y, -1, -1):
                if dp[x][y]:
                    dp[min(X, x+AB[i][0])][min(Y, y+AB[i][1])] = True
    ans = -1
    for x in range(X, X+1):
        for y in range(Y, Y+1):
            if dp[x][y]:
                ans = max(ans, x+y)
    print(ans)

=======
Suggestion 7

def get_min_box_num(box_num, x, y, a, b):
    min_box_num = 9999999
    for i in range(box_num):
        if a[i] >= x and b[i] >= y:
            min_box_num = min(min_box_num, i+1)
    return min_box_num

=======
Suggestion 8

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    dp = [[[False for k in range(Y+1)] for j in range(X+1)] for i in range(N+1)]
    dp[0][0][0] = True
    for i in range(N):
        for j in range(X+1):
            for k in range(Y+1):
                if dp[i][j][k]:
                    dp[i+1][j][k] = True
                    if j+A[i]<=X and k+B[i]<=Y:
                        dp[i+1][j+A[i]][k+B[i]] = True
    #print(dp)
    if dp[N][X][Y]:
        for i in range(N, 0, -1):
            if dp[i-1][X][Y]:
                continue
            else:
                print(i)
                break
    else:
        print(-1)
main()

=======
Suggestion 9

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0 for i in range(Y+1)] for j in range(X+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(X,-1,-1):
            for k in range(Y,-1,-1):
                if dp[j][k] == 1:
                    dp[min(j+A[i],X)][min(k+B[i],Y)] = 1
    for i in range(X+1):
        for j in range(Y+1):
            if dp[X-i][Y-j] == 1:
                print(N-i)
                exit()
    print(-1)
