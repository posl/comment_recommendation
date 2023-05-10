def problem105_b(n):
    # print(n)
    if n % 4 == 0 or n % 7 == 0:
        return 'Yes'
    else:
        for i in range(1, n // 4 + 1):
            if (n - i * 4) % 7 == 0:
                return 'Yes'
        return 'No'
