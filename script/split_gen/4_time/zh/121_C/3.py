def solve(n,m,ab):
    # 二分法
    # ab.sort(key=lambda x:x[0]/x[1],reverse=True)
    # print(ab)
    # sum = 0
    # for i in range(n):
    #     if m == 0:
    #         break
    #     if m < ab[i][1]:
    #         sum += ab[i][0] / ab[i][1] * m
    #         m = 0
    #     else:
    #         sum += ab[i][0]
    #         m -= ab[i][1]
    # return sum
    # 贪心
    ab.sort(key=lambda x:x[0],reverse=True)
    sum = 0
    for i in range(n):
        if m == 0:
            break
        if m < ab[i][1]:
            sum += ab[i][0] * m
            m = 0
        else:
            sum += ab[i][0] * ab[i][1]
            m -= ab[i][1]
    return sum
