def get_count(N, a):
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if min(a[i], a[j]) == i+1 and max(a[i], a[j]) == j+1:
                count += 1
    return count
