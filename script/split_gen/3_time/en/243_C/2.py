def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()
    if N == 2:
        if S == 'RR' or S == 'LL':
            print('No')
        else:
            print('Yes')
        return
    R = []
    L = []
    for i in range(N):
        if S[i] == 'R':
            R.append(i)
        else:
            L.append(i)
    if len(R) == 0 or len(L) == 0:
        print('No')
        return
    if len(R) == 1:
        if X[R[0]] < X[L[0]]:
            print('No')
        else:
            print('Yes')
        return
    if len(L) == 1:
        if X[L[0]] < X[R[0]]:
            print('No')
        else:
            print('Yes')
        return
    R.sort(key=lambda x: X[x])
    L.sort(key=lambda x: X[x])
    if X[R[0]] < X[L[-1]]:
        print('Yes')
        return
    if X[L[0]] < X[R[-1]]:
        print('Yes')
        return
    print('No')
