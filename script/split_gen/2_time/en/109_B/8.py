def shiritori(N, W):
    if N == 1:
        return "Yes"
    else:
        for i in range(1, N):
            if W[i] in W[:i] or W[i][0] != W[i-1][-1]:
                return "No"
        return "Yes"
