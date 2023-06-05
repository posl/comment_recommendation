def main():
    # 读取输入
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 解决问题
    # 用一个布尔数组来记录是否已经使用过某个招数
    used = [False] * (H + 1)
    # 用一个变量来记录当前的健康值
    health = H
    # 用一个变量来记录当前的招数序号
    i = 0
    while True:
        # 如果当前的招数序号超过了招数种类的最大值，那么就说明
        # 无法再继续战斗了（健康值不会再减少了），所以判断
        # 健康值是否已经降到了0以下，如果是则返回Yes，否则
        # 返回No
        if i >= N:
            return "Yes" if health <= 0 else "No"
        # 如果当前的健康值已经降到了0以下，那么说明已经赢得了
        # 战斗，所以返回Yes
        if health <= 0:
            return "Yes"
        # 如果当前的健康值已经降到了0以上，但是招数已经用完了
        # 那么说明已经输掉了战斗，所以返回No
        if i >= N:
            return "No"
        # 如果当前的健康值还大于0，且招数还没有用完，那么就
        # 选择一个招数来使用，如果这个招数已经使用过了，那么
        # 就换一个招数来使用，直到找到一个没有使用过的招数
        while used[i]:
            i += 1
        # 使用招数i
        health -= A[i]
        # 记录招数i已经使用过了
        used[i] = True

if __name__ == '__main__':
    main()