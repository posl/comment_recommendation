def solve():
    import sys
    N = int(sys.stdin.readline())
    A = map(int, sys.stdin.readline().split())
    A = [a % 200 for a in A]
    # 一组数的和的模数的所有可能
    sum_mods = [[] for _ in range(200)]
    for i, a in enumerate(A):
        sum_mods[a].append(i)
    # 一组数的和的模数的所有可能的笛卡尔积
    sum_mods_product = [[] for _ in range(200)]
    for i in range(200):
        for j in range(i + 1, 200):
            for x in sum_mods[i]:
                for y in sum_mods[j]:
                    sum_mods_product[(i + j) % 200].append((x, y))
    # 一组数的和的模数的所有可能的笛卡尔积的所有子集
    sum_mods_product_subset = [[] for _ in range(200)]
    for i in range(200):
        for j in range(1, len(sum_mods_product[i]) + 1):
            for k in range(len(sum_mods_product[i]) - j + 1):
                sum_mods_product_subset[i].append(sum_mods_product[i][k:k + j])
    # 一组数的和的模数的所有可能的笛卡尔积的所有子集的所有和的模数
    sum_mods_product_subset_sum_mods = [[] for _ in range(200)]
    for i in range(200):
        for subset in sum_mods_product_subset[i]:
            sum_mod = sum(A[x] for x in subset) % 200
            if sum_mods_product_subset_sum_mods[sum_mod] == []:
                sum_mods_product_subset_sum_mods[sum_mod].append(subset)
            else:
                print("有")
                print(len(sum_mods_product_subset_sum_mods[sum_mod][0]), *sum_mods_product_subset_sum_mods[sum_mod][0])
                print(len(subset), *subset)
                return
    print("No")
solve()
