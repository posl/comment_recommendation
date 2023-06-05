def solve(n, m, a):
    # 1. 从大到小排序
    # 2. 从大到小排列的数字拼接起来
    # 3. 从大到小排列的数字拼接起来后，如果大于n，则去掉最后一个数字，再判断
    # 4. 如果小于n，则去掉最后一个数字，再判断
    # 5. 如果等于n，则直接返回
    # 1. 从大到小排序
    a.sort(reverse=True)
    # 2. 从大到小排列的数字拼接起来
    num = ''
    for i in range(m):
        num += str(a[i])
    # 3. 从大到小排列的数字拼接起来后，如果大于n，则去掉最后一个数字，再判断
    while int(num) > n:
        num = num[:-1]
    # 4. 如果小于n，则去掉最后一个数字，再判断
    while int(num) < n:
        num = num[:-1]
    # 5. 如果等于n，则直接返回
    return num
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))
