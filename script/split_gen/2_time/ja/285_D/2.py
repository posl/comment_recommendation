def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    #print(S)
    #print(T)
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == T[j] and T[i] == S[j]:
                print("Yes")
                return
    print("No")
    return
