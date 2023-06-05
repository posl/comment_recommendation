def getMinNumOfMagic(N, towns):
    # 1. 遍历所有城镇，计算城镇 i 到城镇 j 的距离，保存到数组中
    # 2. 遍历数组，计算数组中的元素的最大公约数
    # 3. 计算数组中的元素的最大公约数的最大公约数
    # 4. 返回最大公约数的最大公约数
    distance = []
    for i in range(0, N):
        for j in range(i+1, N):
            distance.append(abs(towns[i][0]-towns[j][0])+abs(towns[i][1]-towns[j][1]))
    # print(distance)
    # 2. 遍历数组，计算数组中的元素的最大公约数
    def getGCD(a, b):
        if b == 0:
            return a
        else:
            return getGCD(b, a%b)
    gcd = distance[0]
    for i in range(1, len(distance)):
        gcd = getGCD(gcd, distance[i])
    return gcd
