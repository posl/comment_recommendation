def main():
    #input
    N, X = map(int, input().split())
    S = input()
    #compute
    for i in range(N):
        if S[i] == 'o':
            X += 1
        else:
            if X > 0:
                X -= 1
    #output
    print(X)
