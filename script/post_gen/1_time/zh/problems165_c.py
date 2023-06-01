Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def max_score(N, M, Q, b):
    if Q == 0:
        return 0

    # print("N: %d, M: %d, Q: %d" % (N, M, Q))
    # print(b)
    # print()

    # 1. 先计算出每个位置的最大值
    # 2. 然后计算出每个位置的最大值的和
    # 3. 然后计算出每个位置的最大值的和的最大值
    # 4. 然后计算出每个位置的最大值的和的最大值的最大值
    # 5. 然后计算出每个位置的最大值的和的最大值的最大值的最大值
    # 6. 然后计算出每个位置的最大值的和的最大值的最大值的最大值的最大值
    # 7. 然后计算出每个位置的最大值的和的最大值的最大值的最大值的最大值的最大值
    # 8. 然后计算出每个位置的最大值的和的最大值的最大值的最大值的最大值的最大值的最大值
    # 9. 然后计算出每个位置的最大值的和的最大值的最大值的最大值的最大值的最大值的最大值的最大值
    # 10. 然后计算出每个位置的最大值的和的最大值的最大值的最大值的最大值的最大值的最大值的最大值的最大值
    # 11. 然后计算出每个位置的最大值的和的最大值的��

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())

    ans = 0
    A = [1] * N
    while True:
        score = 0
        for i in range(Q):
            if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                score += d[i]
        ans = max(ans, score)

        idx = N - 1
        while idx >= 0 and A[idx] == M:
            idx -= 1
        if idx < 0:
            break
        A[idx] += 1
        for j in range(idx + 1, N):
            A[j] = A[idx]

    print(ans)

=======
Suggestion 4

def calcScore(A, Q):
    score = 0
    for i in range(len(Q)):
        if (A[Q[i][1]-1] - A[Q[i][0]-1]) == Q[i][2]:
            score += Q[i][3]
    return score

=======
Suggestion 5

def main():
    # 读入数据
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]
    # 算法
    # 从1开始，每次递增1，直到m
    # 1. 先把所有的数都填上1
    # 2. 从最后一位开始，逐个递增，直到满足条件
    # 3. 递增前一位，重复2
    # 4. 递增前一位，重复2
    # 5. 递增前一位，重复2
    # 6. 递增前一位，重复2
    # 7. 递增前一位，重复2
    # 8. 递增前一位，重复2
    # 9. 递增前一位，重复2
    # 10. 递增前一位，重复2
    # 11. 递增前一位，重复2
    # 12. 递增前一位，重复2
    # 13. 递增前一位，重复2
    # 14. 递增前一位，重复2
    # 15. 递增前一位，重复2
    # 16. 递增前一位，重复2
    # 17. 递增前一位，重复2
    # 18. 递增前一位，重复2
    # 19. 递增前一位，重复2
    # 20. 递增前一位，重复2
    # 21. 递增前一位，重复2
    # 22. 递增前一位，重复2
    # 23. 递增前一位，重复2
    # 24. 递增前一位，重复2
    # 25. 递增前一位，重

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(Q)]
    A = [1]
    max_score = 0
    while A[0] <= M:
        if len(A) == N:
            score = 0
            for i in range(Q):
                if A[data[i][1]-1] - A[data[i][0]-1] == data[i][2]:
                    score += data[i][3]
            if score > max_score:
                max_score = score
        A[-1] += 1
        for i in range(len(A)-1, 0, -1):
            if A[i] > M:
                A[i-1] += 1
                A[i] = A[i-1]
    print(max_score)

=======
Suggestion 7

def main():
    n, m, q = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(q):
        a_i, b_i, c_i, d_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
        d.append(d_i)
    max_score = 0
    for i1 in range(1, m+1):
        for i2 in range(i1, m+1):
            for i3 in range(i2, m+1):
                for i4 in range(i3, m+1):
                    for i5 in range(i4, m+1):
                        for i6 in range(i5, m+1):
                            for i7 in range(i6, m+1):
                                for i8 in range(i7, m+1):
                                    for i9 in range(i8, m+1):
                                        for i10 in range(i9, m+1):
                                            score = 0
                                            for i in range(q):
                                                if (b[i] == 1):
                                                    if (i1 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 2):
                                                    if (i2 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 3):
                                                    if (i3 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 4):
                                                    if (i4 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 5):
                                                    if (i5 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 6):
                                                    if (i6 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 7):
                                                    if (i7 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 8):
                                                    if (i8 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 9):
                                                    if (i9 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 10):
                                                    if (i10

=======
Suggestion 8

def main():
    N, M, Q = map(int, input().split())
    AB = []
    CD = []
    for i in range(Q):
        a, b, c, d = map(int, input().split())
        AB.append([a, b])
        CD.append([c, d])
    # print(AB)
    # print(CD)
    # print(N, M, Q)
    # print(AB[1][0])
    # print(CD[1][0])
    # print(AB[2][0])
    # print(CD[2][0])
    # print(AB[3][0])
    # print(CD[3][0])
    # print(AB[4][0])
    # print(CD[4][0])
    # print(AB[5][0])
    # print(CD[5][0])
    # print(AB[6][0])
    # print(CD[6][0])
    # print(AB[7][0])
    # print(CD[7][0])
    # print(AB[8][0])
    # print(CD[8][0])
    # print(AB[9][0])
    # print(CD[9][0])
    # print(AB[10][0])
    # print(CD[10][0])
    # print(AB[11][0])
    # print(CD[11][0])
    # print(AB[12][0])
    # print(CD[12][0])
    # print(AB[13][0])
    # print(CD[13][0])
    # print(AB[14][0])
    # print(CD[14][0])
    # print(AB[15][0])
    # print(CD[15][0])
    # print(AB[16][0])
    # print(CD[16][0])
    # print(AB[17][0])
    # print(CD[17][0])
    # print(AB[18][0])
    # print(CD[18][0])
    # print(AB[19][0])
    # print(CD[19][0])
    # print(AB[20][0])
    # print(CD[20][0])
    # print(AB[21][0])
    # print(CD[
