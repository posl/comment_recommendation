def find_unique_triple(n, a):
    # 1. 首先将a中的元素进行排序
    a.sort()
    print("a = ", a)
    # 2. 从a中找出不同的元素，以及每个元素出现的次数
    unique_a = []
    count_a = []
    for i in range(0, n):
        if a[i] not in unique_a:
            unique_a.append(a[i])
            count_a.append(1)
        else:
            count_a[-1] += 1
    print("unique_a = ", unique_a)
    print("count_a = ", count_a)
    # 3. 计算满足条件的三联体的数量
    unique_count = len(unique_a)
    sum_count = sum(count_a)
    # 3.1 计算满足条件的三联体的数量
    triple_count = 0
    for i in range(0, unique_count-2):
        for j in range(i+1, unique_count-1):
            for k in range(j+1, unique_count):
                triple_count += count_a[i]*count_a[j]*count_a[k]
    # 3.2 计算满足条件的三联体的数量
    for i in range(0, unique_count-1):
        for j in range(i+1, unique_count):
            triple_count += count_a[i]*(count_a[i]-1)*count_a[j]//2
    # 3.3 计算满足条件的三联体的数量
    for i in range(0, unique_count):
        triple_count += count_a[i]*(count_a[i]-1)*(count_a[i]-2)//6
    # 4. 返回满足条件的三联体的数量
    return triple_count
