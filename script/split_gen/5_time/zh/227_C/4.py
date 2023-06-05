def count(N):
    count = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            for k in range(j, N+1):
                if i * j * k <= N:
                    count += 1
                else:
                    break
    return count
