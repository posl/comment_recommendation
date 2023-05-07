def main():
    import sys
    N = int(sys.stdin.readline())
    S = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
    T = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
    if N == 1:
        print('Yes')
    elif N == 2:
        if (T[0][0] - S[0][0]) * (T[1][1] - S[1][1]) == (T[1][0] - S[1][0]) * (T[0][1] - S[0][1]):
            print('Yes')
        else:
            print('No')
    else:
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                else:
                    x = T[0][0] - S[i][0]
                    y = T[0][1] - S[i][1]
                    if S[j][0] + x == T[1][0] and S[j][1] + y == T[1][1]:
                        break
            else:
                continue
            break
        else:
            print('No')
            return
        for i in range(N):
            if S[i][0] + x != T[i][0] or S[i][1] + y != T[i][1]:
                print('No')
                return
        print('Yes')
