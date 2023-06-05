def get_min_time(N, S):
    time = 0
    for i in range(N):
        #print(S[i])
        time = time + get_min_time_for_one(S[i])
    return time
