def solve(n, q, a, x, k):
    result = []
    for i in range(q):
        count = 0
        for j in range(n):
            if a[j] == x[i]:
                count += 1
            if count == k[i]:
                result.append(j+1)
                break
        if count < k[i]:
            result.append(-1)
    return result
