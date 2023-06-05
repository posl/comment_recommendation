def isEnoughWater(N, W, S, T, P):
    #按时间顺序，每次加水，判断是否满足
    #S, T, P = sorted(zip(S, T, P), key=lambda x:x[0])
    #print(S, T, P)
    #print(zip(S, T, P))
    #print(list(zip(S, T, P)))
    for i in range(N):
        water = 0
        for j in range(i + 1):
            if S[j] <= i and i < T[j]:
                water += P[j]
        if water > W:
            return False
    return True

if __name__ == '__main__':
    isEnoughWater()