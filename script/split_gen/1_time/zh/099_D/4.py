def min_error():
    N, C = map(int, raw_input().split())
    D = []
    for i in xrange(C):
        D.append(map(int, raw_input().split()))
    C = []
    for i in xrange(N):
        C.append(map(int, raw_input().split()))
    #print D
    #print C
    # 每个颜色的错误度
    count = []
    for i in xrange(3):
        count.append([0] * C)
    for i in xrange(N):
        for j in xrange(N):
            count[(i + j) % 3][C[i][j] - 1] += 1
    #print count
    # 每个颜色的错误度之和
    sum_count = []
    for i in xrange(3):
        sum_count.append(0)
        for j in xrange(C):
            for k in xrange(C):
                sum_count[i] += count[i][j] * count[i][k] * D[j][k]
    #print sum_count
    # 最小的错误度之和
    min_sum_count = 0
    for i in xrange(3):
        min_sum_count += sum_count[i]
    #print min_sum_count
    # 重绘方格
    for i in xrange(N):
        for j in xrange(N):
            for k in xrange(3):
                if (i + j) % 3 != k:
                    continue
                min_sum_count2 = 0
                for l in xrange(C):
                    min_sum_count2 += count[k][l] * D[C[i][j] - 1][l]
                C[i][j] = l + 1
                if min_sum_count2 < min_sum_count:
                    min_sum_count = min_sum_count2
                else:
                    C[i][j] = k + 1
    print min_sum_count
