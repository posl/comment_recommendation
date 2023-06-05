def main():
    # n:面条的数量，m:需要的面条的数量
    n, m = map(int, input().split())
    # 面条的长度
    a = list(map(int, input().split()))
    # 需要的面条的长度
    b = list(map(int, input().split()))
    # 如果需要的面条的数量大于面条的数量，则不能完成计划
    if m > n:
        print('No')
        return
    # 面条的长度排序
    a.sort()
    # 需要的面条的长度排序
    b.sort()
    # 面条的长度
    a_index = 0
    # 需要的面条的长度
    b_index = 0
    # 需要的面条的数量
    b_count = 0
    # 遍历需要的面条的长度
    while b_index < m:
        # 如果需要的面条的长度小于面条的长度，则不能完成计划
        if b[b_index] < a[a_index]:
            print('No')
            return
        # 如果需要的面条的长度等于面条的长度，则需要的面条的数量加1
        if b[b_index] == a[a_index]:
            b_count += 1
            # 如果需要的面条的数量大于面条的数量，则不能完成计划
            if b_count > n:
                print('No')
                return
            # 如果需要的面条的数量等于面条的数量，则计划完成
            if b_count == n:
                print('Yes')
                return
            # 如果需要的面条的数量没有等于面条的数量，则面条的长度加1
            a_index += 1
        # 如果需要的面条的长度大于面条的长度，则面条的长度加1
        b_index += 1
    # 如果需要的面条的数量没有等于面条的数量，则不能完成计划
    if b_count != n:
        print('No')
        return

if __name__ == '__main__':
    main()