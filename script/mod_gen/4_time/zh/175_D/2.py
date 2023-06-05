def main():
    # 读入数据
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # 从1开始编号，所以减1
    for i in range(N):
        P[i] -= 1
    # 一个周期的和
    cycle_sum = []
    # 一个周期的长度
    cycle_length = []
    # 一个周期的和
    for i in range(N):
        # 已经访问过的编号
        seen = []
        # 棋子的编号
        v = i
        # 一个周期的和
        cycle = 0
        # 一个周期的长度
        length = 0
        while True:
            seen.append(v)
            cycle += C[v]
            length += 1
            v = P[v]
            if v in seen:
                break
        cycle_sum.append(cycle)
        cycle_length.append(length)
    # 答案
    ans = -10 ** 18
    # 一个周期一个周期地考虑
    for i in range(N):
        # 一个周期的和
        s = 0
        # 一个周期的长度
        l = 0
        # 从i开始，最多走K步
        for j in range(min(K, cycle_length[i])):
            s += C[P[i]]
            i = P[i]
            l += 1
            ans = max(ans, s)
            # 如果可以继续走，那么就看看走下去的话，可以得到多少分
            if K - j - 1 > 0:
                # 剩下的步数
                r = K - j - 1
                # 剩下的步数里，可以走的周期数
                q = r // cycle_length[i]
                # 剩下的步数里，可以走的周期以外的步数
                w = r % cycle_length[i]
                # 周期的和
                t = cycle_sum[i] * q
                # 周期以外的和
                if w > 0:
                    t += max(cycle

if __name__ == '__main__':
    main()