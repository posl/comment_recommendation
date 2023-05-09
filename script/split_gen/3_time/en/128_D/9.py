def max_jewel_value(N, K, V):
    max_value = 0
    for i in range(min(K, N)+1):
        for j in range(min(K-i, N-i)+1):
            if i+j > N:
                break
            temp = V[:i] + V[N-j:]
            temp.sort()
            for k in range(min(K-i-j, len(temp))):
                if temp[k] < 0:
                    temp[k] = 0
            max_value = max(max_value, sum(temp))
    return max_value
