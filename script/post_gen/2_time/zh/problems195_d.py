Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, m, q, w, v, x, l, r):
    ans = 0
    for i in range(1, 2**n):
        if bin(i).count('1') != m:
            continue
        weight = 0
        value = 0
        for j in range(n):
            if i & (1 << j):
                weight += w[j]
                value += v[j]
        for j in range(m):
            if x[j] >= weight and l <= j+1 and j+1 <= r:
                ans = max(ans, value)
    return ans

=======
Suggestion 2

def get_max_value(w, v, x):
    # w: weight
    # v: value
    # x: box size
    # return: max value
    dp = [[0 for _ in range(10001)] for _ in range(51)]
    for i in range(1, len(w)+1):
        for j in range(1, 10001):
            if j < w[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
    # print(dp)
    return dp[len(w)][x]

=======
Suggestion 3

def solve():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        ans = 0
        for j in range(M):
            if j < L or j > R:
                ans += X[j]
        dp = [[0 for _ in range(ans+1)] for _ in range(N+1)]
        for i in range(N):
            for j in range(ans+1):
                if j - X[i] >= 0:
                    dp[i+1][j] = max(dp[i][j], dp[i][j-X[i]]+V[i])
                else:
                    dp[i+1][j] = dp[i][j]
        print(dp[N][ans])

=======
Suggestion 4

def main():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    query = [list(map(int,input().split())) for _ in range(q)]
    for l,r in query:
        box = x[:l-1]+x[r:]
        box.sort()
        box.reverse()
        ans = 0
        for w,v in wv:
            for i in range(len(box)):
                if box[i] >= w:
                    ans += v
                    box.pop(i)
                    break
        print(ans)

=======
Suggestion 5

def main():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    query = [list(map(int,input().split())) for _ in range(q)]
    ans = []
    for L,R in query:
        box = x[:L-1]+x[R:]
        box.sort()
        wv.sort(key=lambda x: x[1],reverse=True)
        res = 0
        for i in range(n):
            for j in range(len(box)):
                if wv[i][0]<=box[j]:
                    res += wv[i][1]
                    box.pop(j)
                    break
        ans.append(res)
    for i in ans:
        print(i)

=======
Suggestion 6

def solve(n, m, q, w, v, x, query):
    # dp[i][j][k]表示前i件物品中，放入j个箱子，且第j个箱子放入第k件物品的最大价值
    dp = [[[0 for k in range(n + 1)] for j in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, n + 1):
                if k == i and x[j - 1] >= w[i - 1]:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k - 1] + v[i - 1])
                else:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])
    res = []
    for i in range(q):
        l, r = query[i]
        tmp = 0
        for j in range(1, n + 1):
            tmp = max(tmp, dp[j][r][j])
        res.append(tmp)
    return res

=======
Suggestion 7

def solve():
    # 读入行李数，箱子数，查询数
    n, m, q = map(int, input().split())
    # 读入行李的大小和价值
    wv = [list(map(int, input().split())) for _ in range(n)]
    # 读入箱子的大小
    x = list(map(int, input().split()))
    # 读入查询
    query = [list(map(int, input().split())) for _ in range(q)]

    # 箱子的大小降序排列
    x.sort(reverse=True)

    # 箱子的大小，行李的大小，行李的价值
    dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(m + 1)]

    # 遍历箱子
    for i in range(m):
        # 遍历行李
        for j in range(n):
            # 遍历行李的价值
            for k in range(wv[j][1], m + 1):
                # 更新dp
                dp[i + 1][k][j + 1] = max(dp[i + 1][k][j + 1], dp[i][k - wv[j][1]][j] + wv[j][0])

    # 遍历查询
    for l, r in query:
        # 初始化箱子的大小
        y = x[:l - 1] + x[r:]
        # 箱子的大小降序排列
        y.sort(reverse=True)
        # 初始化答案
        ans = 0
        # 遍历箱子
        for i in range(m):
            # 遍历行李
            for j in range(n):
                # 遍历行李的价值
                for k in range(wv[j][1], m + 1):
                    # 更新答案
                    ans = max(ans, dp[i + 1][k][j + 1])
        # 打印答案
        print(ans)


solve()

=======
Suggestion 8

def isok(baggage,box):
    baggage.sort(key=lambda x:x[1],reverse=True)
    box.sort(reverse=True)
    for i in box:
        for j in range(len(baggage)):
            if i>=baggage[j][0]:
                box.remove(i)
                baggage.remove(baggage[j])
                break
    if len(baggage)==0:
        return True
    else:
        return False

=======
Suggestion 9

def main():
    n,m,q = map(int,input().split())
    wv = []
    for i in range(n):
        wv.append(list(map(int,input().split())))
    x = list(map(int,input().split()))
    query = []
    for i in range(q):
        query.append(list(map(int,input().split())))
    for i in range(q):
        l = query[i][0]
        r = query[i][1]
        x_copy = x.copy()
        x_copy.pop(l-1)
        x_copy.pop(r-2)
        x_copy.sort(reverse=True)
        wv_copy = wv.copy()
        wv_copy.sort(key=lambda x:x[1],reverse=True)
        #print(wv_copy)
        #print(x_copy)
        for j in range(len(x_copy)):
            for k in range(len(wv_copy)):
                if wv_copy[k][0] <= x_copy[j]:
                    wv_copy.pop(k)
                    break
        #print(wv_copy)
        sum = 0
        for j in range(len(wv_copy)):
            sum += wv_copy[j][1]
        print(sum)

=======
Suggestion 10

def main():
    n,m,q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(n)]
    x = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(q)]
    ans = [0] * q
    for i in range(q):
        l, r = queries[i]
        boxes = x[:l-1] + x[r:]
        boxes.sort()
        boxes = boxes[::-1]
        boxes = boxes[:n]
        boxes.sort()
        boxes = boxes[::-1]
        boxes = boxes[:n]
        wv.sort(key=lambda x:x[1], reverse=True)
        for j in range(n):
            for k in range(n):
                if wv[k][0] <= boxes[j]:
                    ans[i] += wv[k][1]
                    wv[k][0] = 10**9
                    break

    for i in range(q):
        print(ans[i])
