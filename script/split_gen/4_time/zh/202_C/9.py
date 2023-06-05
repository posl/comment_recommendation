def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    # 1. 暴力
    # ans = 0
    # for i in range(n):
    #     for j in range(n):
    #         if a[i] == b[c[j]-1]:
    #             ans += 1
    # print(ans)
    # 2. 哈希表
    # ans = 0
    # c_dict = {}
    # for i in range(n):
    #     if c[i] not in c_dict:
    #         c_dict[c[i]] = 1
    #     else:
    #         c_dict[c[i]] += 1
    #
    # for i in range(n):
    #     if a[i] in c_dict:
    #         ans += c_dict[a[i]]
    #
    # print(ans)
    # 3. 二分查找
    # ans = 0
    # c.sort()
    # for i in range(n):
    #     if a[i] in c:
    #         # 二分查找
    #         left = 0
    #         right = n - 1
    #         while left <= right:
    #             mid = (left + right) // 2
    #             if c[mid] == a[i]:
    #                 ans += 1
    #                 break
    #             elif c[mid] < a[i]:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    # print(ans)
    # 4. 二分查找
    ans = 0
    c.sort()
    for i in range(n):
        if a[i] in c:
            # 二分查找
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if c[mid] == a[i]:
                    ans += 1
                    # 从c中删除匹配的元素，防止重复计数
                    del c[mid]
                    break
                elif c[mid] < a[i]:
