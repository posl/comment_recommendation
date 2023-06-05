def is_permutation(array):
    # 从小到大排序
    array.sort()
    # 检查是否为1到N的连续数列
    for i in range(len(array)):
        if array[i] != i + 1:
            return False
    return True
n = int(input())
a = list(map(int, input().split()))
