def solve(n, a):
    # 递归
    # 递归的终止条件
    if n == 1:
        return a.index(min(a)) + 1
    # 递归的递推公式
    # 1.找到a中最大的数，和它的下标
    max_num = max(a)
    max_index = a.index(max_num)
    # 2.找到它的对手的下标
    # 2.1 确定当前轮的比赛的总人数
    total = 2 ** n
    # 2.2 确定当前轮的比赛的人数
    current = total // 2
    # 2.3 确定当前轮的比赛的人数的一半
    half = current // 2
    # 2.4 确定当前轮的比赛的人数的一半的一半
    half_half = half // 2
    # 2.5 确定当前轮的比赛的人数的一半的一半的一半
    half_half_half = half_half // 2
    # 2.6 确定当前轮的比赛的人数的一半的一半的一半的一半
    half_half_half_half = half_half_half // 2
    # 2.7 确定当前轮的比赛的人数的一半的一半的一半的一半的一半
    half_half_half_half_half = half_half_half_half // 2
    # 2.8 确定当前轮的比赛的人数的一半的一半的一半的一半的一半的一半
    half_half_half_half_half_half = half_half_half_half_half // 2
    # 2.9 确定当前轮的比赛的人数的一半的一半的一半的一半的一半的一半的一

if __name__ == '__main__':
    solve()