def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #print(N)
    #print(S)
    # 横方向
    for i in range(N):
        cnt = 0
        for j in range(N):
            if S[i][j] == '#':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print('Yes')
                    exit()
    # 縦方向
    for j in range(N):
        cnt = 0
        for i in range(N):
            if S[i][j] == '#':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print('Yes')
                    exit()
    # 斜め方向
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i + j >= N:
                break
            if S[i+j][j] == '#':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print('Yes')
                    exit()
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i + j >= N:
                break
            if S[j][i+j] == '#':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print('Yes')
                    exit()
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i - j < 0:
                break
            if S[i-j][j] == '#':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print('Yes')
                    exit()
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i - j < 0:
                break
            if S[j][i-j] == '#':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print('Yes')
                    exit()
    print('No')
