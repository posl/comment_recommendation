def get_max_value(N, K, V):
    max_value = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i+j <= N and i+j <= K:
                temp = 0
                for k in range(i):
                    temp += V[k]
                for k in range(N-j, N):
                    temp += V[k]
                if temp > max_value:
                    max_value = temp
    return max_value
