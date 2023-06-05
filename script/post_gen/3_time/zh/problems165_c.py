Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n,m,q=map(int,input().split())
    abcd=[]
    for i in range(q):
        abcd.append(list(map(int,input().split())))
    print(abcd)
    print(n,m,q)
    #print(a,b,c,d)

=======
Suggestion 3

def get_max_score(N, M, Q, array):
    # 从小到大排序
    array = sorted(array)
    # 记录每个位置的值
    value = [0 for i in range(N)]
    for i in range(N):
        value[i] = i + 1
    # 记录每个位置的值的总和
    sum = [0 for i in range(N)]
    for i in range(N):
        sum[i] = i + 1
    # 记录每个位置的值的总和的最大值
    max_sum = 0
    # 记录每个位置的值的总和的最大值的位置
    max_sum_index = 0
    # 记录每个位置的值的总和的最小值
    min_sum = 0
    # 记录每个位置的值的总和的最小值的位置
    min_sum_index = 0
    # 记录每个位置的值的总和的最大值的位置
    max_sum = 0
    # 记录每个位置的值的总和的最大值的位置
    max_sum_index = 0
    for i in range(Q):
        a = array[i][0]
        b = array[i][1]
        c = array[i][2]
        d = array[i][3]
        for j in range(a - 1, b):
            value[j] += c
            sum[j] += d
        if (max_sum < sum[b - 1]):
            max_sum = sum[b - 1]
            max_sum_index = b - 1
        if (min_sum > sum[a - 1]):
            min_sum = sum[a - 1]
            min_sum_index = a - 1
    sum[max_sum_index] = 0
    sum[min_sum_index] = 0
    for i in range(N):
        if (max_sum < sum[i]):
            max_sum = sum[i]
    return max_sum

=======
Suggestion 4

def get_max_score(n, m, q, a, b, c, d):
    score = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                for l in range(1, n + 1):
                    if i <= j <= k <= l:
                        score += d[i] + d[j] + d[k] + d[l]
    return score

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    for A in combinations_with_replacement(range(1,M+1),N):
        score = 0
        for a,b,c,d in query:
            if A[b-1]-A[a-1] == c:
                score += d
        ans = max(ans,score)
    print(ans)

=======
Suggestion 6

def main():
    n,m,q = map(int,input().split())
    a = [0] * (n+1)
    b = [0] * (n+1)
    c = [0] * (n+1)
    d = [0] * (n+1)
    for i in range(q):
        a[i],b[i],c[i],d[i] = map(int,input().split())
    print(a)
    print(b)
    print(c)
    print(d)
    return 0

=======
Suggestion 7

def solve():
    pass

=======
Suggestion 8

def max_score(n, m, q, score):
    max_score = 0
    for i in range(1, m+1):
        for j in range(1, m+1):
            for k in range(1, m+1):
                for l in range(1, m+1):
                    s = 0
                    for x in range(0, q):
                        if score[x][1] - score[x][0] == i:
                            s += score[x][2]
                        if score[x][1] - score[x][0] == j:
                            s += score[x][2]
                        if score[x][1] - score[x][0] == k:
                            s += score[x][2]
                        if score[x][1] - score[x][0] == l:
                            s += score[x][2]
                    if max_score < s:
                        max_score = s
    return max_score
