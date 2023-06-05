def main():
    N,M,Q = map(int,input().split())
    LR = []
    for i in range(M):
        LR.append(list(map(int,input().split())))
    pq = []
    for i in range(Q):
        pq.append(list(map(int,input().split())))
    for i in range(Q):
        count = 0
        for j in range(M):
            if pq[i][0] <= LR[j][0] and LR[j][1] <= pq[i][1]:
                count += 1
        print(count)
