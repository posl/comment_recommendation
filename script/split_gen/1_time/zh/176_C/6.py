def solve(n, a):
    # 从左到右遍历，记录目前为止最高的人的高度
    # 只有当当前人的高度小于目前为止最高的人的高度时，才需要站在目前为止最高的人的头上
    # 因为如果当前人的高度大于目前为止最高的人的高度，那么当前人就可以站在地上了
    # 这样就不需要站在目前为止最高的人的头上了
    # 这样就可以保证站在目前为止最高的人的头上的人的高度是非递减的
    # 这样就可以保证每个人的高度都不小于前面的人的高度
    max_height = 0
    ans = 0
    for i in range(n):
        if a[i] < max_height:
            ans += max_height - a[i]
        else:
            max_height = a[i]
    return ans
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
