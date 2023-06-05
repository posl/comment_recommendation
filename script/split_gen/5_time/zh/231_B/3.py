def main():
    #input
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #process
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
        else:
            D[S[i]] = 1
    #output
    print(max(D, key=D.get))
