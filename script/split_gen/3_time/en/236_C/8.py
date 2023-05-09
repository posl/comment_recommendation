def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    #print(N,M)
    #print(S)
    #print(T)
    #print(S[0])
    #print(T[0])
    #print(S[-1])
    #print(T[-1])
    for i in range(N):
        if S[i] in T:
            print('Yes')
        else:
            print('No')
