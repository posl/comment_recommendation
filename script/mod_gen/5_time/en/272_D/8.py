def main():
    N,M = map(int,input().split())
    M = M**0.5
    M = int(M)
    if M*M == M:
        M = M
    else:
        M = M+1
    if M*M < 2:
        M = 2
    if M*M > 10**6:
        M = 10**6
    ans = []
    for i in range(N):
        ans.append([])
        for j in range(N):
            ans[i].append(-1)
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ans[i][j] == -1:
                continue
            for k in range(-M,M+1):
                for l in range(-M,M+1):
                    if i+k < 0 or i+k >= N or j+l < 0 or j+l >= N:
                        continue
                    if (i+k)**2+(j+l)**2 <= M*M:
                        ans[i+k][j+l] = ans[i][j]+1
    for i in range(N):
        for j in range(N):
            print(ans[i][j],end = " ")
        print()

if __name__ == '__main__':
    main()