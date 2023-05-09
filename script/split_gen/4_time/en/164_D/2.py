def solve(S):
    N = len(S)
    count = 0
    for i in range(N):
        for j in range(i,N):
            if int(S[i:j+1])%2019 == 0:
                count += 1
    return count
