def main():
    # 读取输入
    line = input()
    n, k = line.split()
    n = int(n)
    k = int(k)
    line = input()
    a = line.split()
    # 将输入转换为int
    for i in range(len(a)):
        a[i] = int(a[i])
    # 从1开始遍历
    count = 0
    for i in range(1, n + 1):
        # 找到i的位置
        index = a.index(i)
        # 判断index是否在k-1的范围内
        if index >= k - 1:
            # 如果在k-1的范围内，就将index之前的元素全部替换为i
            for j in range(index - k + 1, index + 1):
                a[j] = i
            # 计数+1
            count += 1
        # 如果不在k-1的范围内
        else:
            # 如果index不为0
            if index != 0:
                # 将index之前的元素全部替换为i
                for j in range(0, index + 1):
                    a[j] = i
                # 计数+1
                count += 1
            # 如果index为0
            else:
                # 将index之后的元素全部替换为i
                for j in range(0, k):
                    a[j] = i
                # 计数+1
                count += 1
    # 输出结果
    print(count)

if __name__ == '__main__':
    main()