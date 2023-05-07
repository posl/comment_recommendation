def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        for j in range(i+1,N):
            if S[i] == S[j] or T[i] == T[j] or S[i] == T[j] or T[i] == S[j]:
                print("No")
                return
    print("Yes")
