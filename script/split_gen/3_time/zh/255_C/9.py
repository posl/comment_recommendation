def main():
    # 读入数据
    X, A, D, N = map(int, input().split())
    # 从A开始往后N个数，组成一个等差数列
    # 用等差数列的求和公式求出最大值
    max = A + (N - 1) * D
    # 用等差数列的求和公式求出最小值
    min = A
    # 如果X在这个区间内，就直接输出0
    if X >= min and X <= max:
        print(0)
        return
    # 如果X小于最小值，就用最小值减去X
    if X < min:
        print(min - X)
        return
    # 如果X大于最大值，就用X减去最大值
    if X > max:
        print(X - max)
        return
main()
