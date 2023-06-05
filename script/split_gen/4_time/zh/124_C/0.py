def minPaint(N, S):
    count = 0
    for i in range(0, N-1):
        if S[i] == S[i+1]:
            count += 1
    return count
