def get_sum(array, k, d):
    # 从array中取k个数，和为d的倍数的最大值
    # 从array中取k个数，和为d的倍数的最大值
    if k == 1:
        if array[0] % d == 0:
            return array[0]
        else:
            return -1
    elif k == 2:
        max_sum = -1
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if (array[i] + array[j]) % d == 0:
                    max_sum = max(max_sum, array[i] + array[j])
        return max_sum
    else:
        max_sum = -1
        for i in range(len(array)):
            temp = get_sum(array[i+1:], k-1, d)
            if temp != -1:
                max_sum = max(max_sum, array[i] + temp)
        return max_sum
line = input().strip()
n, k, d = list(map(int, line.split()))
array = list(map(int, input().strip().split()))
print(get_sum(array, k, d))
