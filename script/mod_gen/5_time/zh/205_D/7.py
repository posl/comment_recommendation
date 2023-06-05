def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    # print(n, q, a, k)
    # 1. 生成不重复的数列
    # 2. 排序
    # 3. 找第k个数
    # 4. 二分查找
    # 5. 递归
    # 6. 线性查找
    # 7. 二分查找
    # 1. 生成不重复的数列
    # 2. 排序
    # 3. 找第k个数
    # 4. 二分查找
    # 5. 递归
    # 6. 线性查找
    # 7. 二分查找
    # 1. 生成不重复的数列
    a_set = set(a)
    a_list = list(a_set)
    a_list.sort()
    # print(a_list)
    # 2. 排序
    # 3. 找第k个数
    # 4. 二分查找
    # 5. 递归
    # 6. 线性查找
    # 7. 二分查找
    # print(a_list)
    for i in k:
        print(a_list[i - 1])

if __name__ == '__main__':
    main()