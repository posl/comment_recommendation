def main():
    # N, M
    N, M = map(int, input().split())
    # A_i, B_i
    AB = [list(map(int, input().split())) for _ in range(M)]
    # K
    K = int(input())
    # C_i, D_i
    CD = [list(map(int, input().split())) for _ in range(K)]
    # print(N, M, AB, K, CD)
    # print(N, M, AB, K, CD)
    max_count = 0
    for i in range(2 ** K):
        # print('i =', i)
        count = 0
        balls = [0] * N
        for j in range(K):
            # print('j =', j)
            # print('i >> j =', i >> j)
            if (i >> j) & 1:
                # print('i >> j & 1 =', i >> j & 1)
                balls[CD[j][0] - 1] += 1
            else:
                balls[CD[j][1] - 1] += 1
        # print('balls =', balls)
        for k in range(M):
            # print('k =', k)
            if balls[AB[k][0] - 1] > 0 and balls[AB[k][1] - 1] > 0:
                count += 1
        # print('count =', count)
        max_count = max(max_count, count)
        # print('max_count =', max_count)
    print(max_count)
