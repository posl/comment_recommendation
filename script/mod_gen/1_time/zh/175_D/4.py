def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(N):
        # 一圈的得分
        score = 0
        # 一圈的步数
        cnt = 0
        # 一圈的开始位置
        j = i
        while True:
            # 走一步
            j = P[j] - 1
            score += C[j]
            cnt += 1
            # 一圈走完了
            if j == i:
                break
        # 一圈的得分
        loop = score
        # 一圈的步数
        loop_cnt = cnt
        # 一圈的开始位置
        loop_start = i
        # 一圈的得分
        score = 0
        # 一圈的步数
        cnt = 0
        # 一圈的开始位置
        j = i
        while True:
            # 走一步
            j = P[j] - 1
            score += C[j]
            cnt += 1
            # 一圈走完了
            if j == i:
                break
        # 一圈的得分
        loop = score
        # 一圈的步数
        loop_cnt = cnt
        # 一圈的开始位置
        loop_start = i
        # 一圈的得分
        score = 0
        # 一圈的步数
        cnt = 0
        # 一圈的开始位置
        j = i
        while True:
            # 走一步
            j = P[j] - 1
            score += C[j]
            cnt += 1
            # 一圈走完了
            if j == i:
                break
        # 一圈的得分
        loop = score
        # 一圈的步数
        loop_cnt = cnt
        # 一圈的开始位置
        loop_start = i
        # 一

if __name__ == '__main__':
    main()