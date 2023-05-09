def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'L':
            X[i] *= -1
    X.sort()
    for i in range(N):
        if S[i] == 'L':
            X[i] *= -1
    for i in range(N):
        if S[i] == 'R':
            for j in range(N):
                if S[j] == 'L' and X[i] < X[j] and Y[i] == Y[j]:
                    print('Yes')
                    return
    print('No')
