def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # print(N, S, W)
    # 二分查找
    # 用于判断当前X下的人是儿童还是成年人
    def check(x):
        # 遍历所有人
        for s, w in zip(S, W):
            # 判断
            if s == '0' and w >= x:
                return True
            elif s == '1' and w < x:
                return True
        return False
    # 二分查找
    def binary_search():
        # 左右边界
        left = 0
        right = 10 ** 9 + 1
        # 循环
        while right - left > 1:
            # 中间值
            mid = (left + right) // 2
            # 判断
            if check(mid):
                left = mid
            else:
                right = mid
        # 返回
        return left
    # 输出
    print(binary_search())
