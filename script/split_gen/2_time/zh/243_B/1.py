def main():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 处理数据
    # 1. 包含在A和B中的整数的数量，出现在两个序列的相同位置
    # 2. 包含在A和B中的整数的数量，出现在两个序列的不同位置
    count1 = 0
    count2 = 0
    for i in range(N):
        if A[i] == B[i]:
            count1 += 1
    for i in range(N):
        for j in range(N):
            if i != j and A[i] == B[j]:
                count2 += 1
    # 输出结果
    print(count1)
    print(count2)
