def triangle(N, L):
    L.sort()
    count = 0
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i] + L[j]:
                    count += 1
    return count
