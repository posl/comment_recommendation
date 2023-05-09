def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(list(map(int, input().split())))
    for i in range(N):
        T.append(list(map(int, input().split())))
    S.sort()
    T.sort()
    for i in range(N):
        for j in range(N):
            a = T[i][0] - S[j][0]
            b = T[i][1] - S[j][1]
            for k in range(N):
                if [S[k][0] + a, S[k][1] + b] in T:
                    continue
                else:
                    break
            else:
                print('Yes')
                exit()
    else:
        print('No')
