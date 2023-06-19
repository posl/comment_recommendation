def getMaxReward(N,M,work):
    work.sort(key=lambda x:x[0])
    work.sort(key=lambda x:x[1],reverse=True)
    #print(work)
    reward = [0 for i in range(M)]
    for i in range(N):
        for j in range(work[i][0]-1,M):
            if reward[j] == 0:
                reward[j] = work[i][1]
                break
    return sum(reward)
