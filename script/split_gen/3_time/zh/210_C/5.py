def solution(N, K, c):
    #print(N, K, c)
    count = 0
    max_count = 0
    for i in range(N):
        if i < K:
            if c[i] not in c[0:i]:
                count += 1
        else:
            if c[i] not in c[i-K:i]:
                count += 1
        if max_count < count:
            max_count = count
        #print("count:", count)
    return max_count
