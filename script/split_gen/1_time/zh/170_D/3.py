def solve():
    n = int(input())
    a = list(map(int, input().split()))
    # 从小到大排序
    a.sort()
    # 用于记录数字i是否为满足条件的数字
    ans = [True for i in range(n)]
    # 从小到大遍历
    for i in range(n):
        # 如果数字i已经被标记为不满足条件的数字，则跳过
        if not ans[i]:
            continue
        # 从小到大遍历
        for j in range(i + 1, n):
            # 如果数字j已经被标记为不满足条件的数字，则跳过
            if not ans[j]:
                continue
            # 如果数字j可以被数字i整除，则标记数字j为不满足条件的数字
            if a[j] % a[i] == 0:
                ans[j] = False
    # 计数满足条件的数字个数
    cnt = 0
    for i in range(n):
        if ans[i]:
            cnt += 1
    print(cnt)
