def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        a, b = map(int, input().split())
        S.append((a, b))
    for i in range(N):
        c, d = map(int, input().split())
        T.append((c, d))
    if N == 1:
        print('Yes')
    else:
        S.sort()
        T.sort()
        for i in range(N):
            for j in range(N):
                dx = T[j][0] - S[i][0]
                dy = T[j][1] - S[i][1]
                for k in range(N):
                    if (S[k][0] + dx, S[k][1] + dy) in T:
                        continue
                    else:
                        break
                else:
                    print('Yes')
                    exit()
        print('No')
