Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    C = list(map(int,input().split()))
    P.insert(0,0)
    C.insert(0,0)
    ans = -float("inf")
    for i in range(1,N+1):
        loop = []
        loop.append(C[i])
        loop.append(C[P[i]])
        loop.append(C[P[P[i]]])
        if K>=3:
            loop.append(C[P[P[P[i]]]])
        if K>=4:
            loop.append(C[P[P[P[P[i]]]]])
        if K>=5:
            loop.append(C[P[P[P[P[P[i]]]]]])
        if K>=6:
            loop.append(C[P[P[P[P[P[P[i]]]]]]])
        if K>=7:
            loop.append(C[P[P[P[P[P[P[P[i]]]]]]]])
        if K>=8:
            loop.append(C[P[P[P[P[P[P[P[P[i]]]]]]]]])
        if K>=9:
            loop.append(C[P[P[P[P[P[P[P[P[P[i]]]]]]]]]])
        if K>=10:

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def solve(n,k,p,c):
    maxScore = -10000000000
    for i in range(n):
        next = p[i]-1
        score = c[next]
        for j in range(k-1):
            next = p[next]-1
            score += c[next]
        if score > maxScore:
            maxScore = score
    return maxScore

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = -float('inf')
    for i in range(N):
        v = i
        s = 0
        t = 0
        while True:
            v = P[v] - 1
            s += C[v]
            t += 1
            if v == i:
                break
            if t == K:
                break
        if s > ans:
            ans = s
    print(ans)

solve()

=======
Suggestion 5

def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(n):
        # i: start point
        # j: end point
        j = i
        s = 0
        t = 0
        while True:
            j = p[j] - 1
            s += c[j]
            t += 1
            if j == i:
                break
            if t == k:
                break
        if s > 0:
            u = s * (k // t - 1)
            ans = max(ans, u + s)
        else:
            ans = max(ans, s)
    print(ans)

=======
Suggestion 6

def solve():
    pass

=======
Suggestion 7

def problems175_d():
    return None

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    #print(n, k, p, c)
    max_score = -1e9
    for i in range(n):
        score = 0
        j = i
        step = 0
        while True:
            j = p[j] - 1
            score += c[j]
            step += 1
            if j == i:
                break
            if step == k:
                break
        if step < k and score > 0:
            score += (k - step) // step * score
        if score > max_score:
            max_score = score
    print(max_score)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [p-1 for p in P]
    # print(P)
    # print(C)

    # 1. 从每个点开始，计算最大得分
    # 2. 从每个点开始，计算最大得分，再走一步，计算最大得分
    # 3. 从每个点开始，计算最大得分，再走两步，计算最大得分
    # 4. 从每个点开始，计算最大得分，再走三步，计算最大得分
    # ...
    # 5. 从每个点开始，计算最大得分，再走K-1步，计算最大得分
    # 6. 取5个中最大的

    # 1. 从每个点开始，计算最大得分
    # 1.1 从每个点开始，计算最大得分
    # 1.2 从每个点开始，计算最大得分
    # 1.3 从每个点开始，计算最大得分
    # 1.4 从每个点开始，计算最大得分
    # ...
    # 1.K-1 从每个点开始，计算最大得分
    # 1.K 取1.K-1个中最大的

    # 2. 从每个点开始，计算最大得分，再走一步，计算最大得分
    # 2.1 从每个点开始，计算最大得分，再走一步，计算最大得分
    # 2.2 从每个点开始，计算最大得分，再走一步，计算最大得分
    # 2.3 从每个点开始，计算最大得分，再走一步，计算最大得分
    # 2.
