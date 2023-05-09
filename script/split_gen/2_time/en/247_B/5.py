def main():
    #input
    N = int(input())
    S = [None] * N
    T = [None] * N
    for i in range(N):
        S[i], T[i] = input().split()
    
    #compute
    for i in range(N):
        if S[i] == T[i]:
            print("No")
            return
        for j in range(N):
            if i != j and (S[i] == S[j] or S[i] == T[j] or T[i] == S[j] or T[i] == T[j]):
                print("No")
                return
    print("Yes")
    
    return
