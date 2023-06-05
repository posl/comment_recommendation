def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    # 负数的个数
    neg = 0
    # 绝对值最小的数
    min_abs = 10**9 + 1
    # 绝对值之和
    sum_abs = 0
    # 计算负数的个数，并且求出绝对值最小的数
    for i in range(N):
        if A[i] < 0:
            neg += 1
        if abs(A[i]) < min_abs:
            min_abs = abs(A[i])
        sum_abs += abs(A[i])
    # 如果负数的个数是偶数，则直接输出绝对值之和
    if neg % 2 == 0:
        print(sum_abs)
    # 如果负数的个数是奇数，则将绝对值之和减去两个最小的绝对值之和
    else:
        print(sum_abs - 2 * min_abs)
