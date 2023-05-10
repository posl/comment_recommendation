def xor_sum(a):
    sum = 0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            sum += a[i] ^ a[j]
    return sum
