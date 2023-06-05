def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(int(t))
    for i in range(N):
        if S[i] == S[i+1]:
            T[i+1] = max(T[i],T[i+1])
            T[i] = 0
    print(T.index(max(T))+1)
