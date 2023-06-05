def happy_people_num(N,K,S):
    happy_num = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy_num += 1
    happy_num = min(happy_num + 2 * K,N-1)
    return happy_num
