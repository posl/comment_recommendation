def getPerm(num, k):
    num.sort()
    k -= 1
    while k > 0:
        for i in range(len(num) - 2, -1, -1):
            if num[i] < num[i + 1]:
                break
        for j in range(len(num) - 1, -1, -1):
            if num[j] > num[i]:
                break
        num[i], num[j] = num[j], num[i]
        num[i + 1:] = num[len(num) - 1:i:-1]
        k -= 1
    return num
