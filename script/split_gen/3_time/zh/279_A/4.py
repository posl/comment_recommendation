def count_d(S):
    count = 0
    for i in range(len(S)):
        if S[i] == "w":
            count += S.count("v", i)
    return count
