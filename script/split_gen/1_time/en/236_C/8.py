def main():
    N,M = map(int,input().split())
    S = input().split()
    T = input().split()
    #print(N,M)
    #print(S)
    #print(T)
    #print("----")
    for i in range(N):
        if S[i] in T:
            print("Yes")
        else:
            print("No")
