def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    S = ''
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    S = input()
    #print(N)
    #print(X)
    #print(Y)
    #print(S)
    #print('==============================')
    if N == 2:
        if S == 'RR' or S == 'LL':
            print('No')
        else:
            print('Yes')
        return
    for i in range(N):
        if S[i] == 'R':
            for j in range(i+1, N):
                if S[j] == 'L':
                    if X[i] < X[j]:
                        print('Yes')
                        return
                    else:
                        break
        else:
            for j in range(i+1, N):
                if S[j] == 'R':
                    if X[i] > X[j]:
                        print('Yes')
                        return
                    else:
                        break
    print('No')
    return
