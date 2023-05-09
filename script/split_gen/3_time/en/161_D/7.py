def solve(K):
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        if len(lunlun) >= K:
            return lunlun[K-1]
        lunlun.append(lunlun[i]*10 + lunlun[i]%10 - 1)
        lunlun.append(lunlun[i]*10 + lunlun[i]%10)
        lunlun.append(lunlun[i]*10 + lunlun[i]%10 + 1)
        lunlun = [x for x in lunlun if 0 < x <= 10**9]
