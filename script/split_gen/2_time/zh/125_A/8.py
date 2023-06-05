def main():
    # 读入数据
    N, K = map(int, input().split())
    S = input()
    # 计算连续站立的人的最大可能数量
    max_count = 0
    count = 0
    for i in range(N):
        if S[i] == "0":
            count += 1
        else:
            if K > 0:
                K -= 1
                count += 1
            else:
                count -= 1
        if count > max_count:
            max_count = count
    # 输出结果
    print(max_count)
