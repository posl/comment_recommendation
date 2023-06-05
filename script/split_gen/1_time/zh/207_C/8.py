def main():
    N = int(input())
    T = []
    for i in range(N):
        T.append(list(map(int,input().split())))
    
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            if T[i][1] <= T[j][1] and T[j][1] <= T[i][2]:
                cnt += 1
            elif T[i][1] <= T[j][2] and T[j][2] <= T[i][2]:
                cnt += 1
            elif T[j][1] <= T[i][1] and T[i][1] <= T[j][2]:
                cnt += 1
            elif T[j][1] <= T[i][2] and T[i][2] <= T[j][2]:
                cnt += 1
    print(cnt)
