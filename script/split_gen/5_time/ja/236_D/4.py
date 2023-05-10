def xor_sum(a):
    result = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            result += a[i]^a[j]
    return result
