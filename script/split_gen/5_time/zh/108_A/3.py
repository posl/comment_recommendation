def problems108_a(k):
    count = 0
    for i in range(1, k+1):
        for j in range(1, k+1):
            if i%2 == 0 and j%2 != 0:
                count += 1
    return count
