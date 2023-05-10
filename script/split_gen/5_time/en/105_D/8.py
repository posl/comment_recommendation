def find_pairs(N, M, A):
    sums = [0] * (N + 1)
    for i in range(N):
        sums[i + 1] = sums[i] + A[i]
    sums = [s % M for s in sums]
    sums.sort()
    count = 1
    result = 0
    for i in range(1, N + 1):
        if sums[i] == sums[i - 1]:
            count += 1
        else:
            result += count * (count - 1) // 2
            count = 1
    result += count * (count - 1) // 2
    return result
