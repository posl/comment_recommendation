def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    S = input()
    for i in range(N):
        X[i],Y[i] = map(int,input().split())
    for i in range(N):
        for j in range(i+1,N):
            if X[i] > X[j]:
                X[i],X[j] = X[j],X[i]
                Y[i],Y[j] = Y[j],Y[i]
                S = S[:i] + S[i+1:j] + S[i] + S[j+1:]
    for i in range(N-1):
        if S[i] == 'R' and S[i+1] == 'L' and X[i] == X[i+1] and Y[i] == Y[i+1]:
            print('Yes')
            return
    print('No')
