def solve(n):
    count = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j >= n:
                break
            else:
                count += 1
    return count
