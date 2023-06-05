def solve(n, m, a, b):
    # 二分查找
    # 二分查找的上下限分别是0和10^9+1
    left = 0
    right = 10**9 + 1
    while left + 1 < right:
        mid = (left + right) // 2
        # 验证mid是否满足条件
        # 用mid元能买到的饮料数
        num = 0
        for i in range(n):
            # 用mid元能买到的饮料数
            if a[i] >= mid:
                num += b[i]
        if num >= m:
            # mid元能买到的饮料数大于等于m，说明mid元太大了，下次查找时mid应该小一些
            right = mid
        else:
            # mid元能买到的饮料数小于m，说明mid元太小了，下次查找时mid应该大一些
            left = mid
    return left

if __name__ == '__main__':
    solve()