def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(int(t))
    #print(S)
    #print(T)
    #print(T[0])
    #print(T[1])
    #print(S[0])
    #print(S[1])
    #print(T[0] > T[1])
    #print(S[0] == S[1])
    #print(T[0] > T[1] and S[0] == S[1])
    #print(T[1] > T[0] and S[1] == S[0])
    #print(T[0] > T[1] and S[0] == S[1] and T[0] > T[2] and S[0] == S[2])
    #print(T[1] > T[0] and S[1] == S[0] and T[1] > T[2] and S[1] == S[2])
    #print(T[2] > T[0] and S[2] == S[0] and T[2] > T[1] and S[2] == S[1])
    #print(T[0] > T[1] and S[0] == S[1] and T[0] > T[2] and S[0] == S[2] and T[0] > T[3] and S[0] == S[3])
    #print(T[1] > T[0] and S[1] == S[0] and T[1] > T[2] and S[1] == S[2] and T[1] > T[3] and S[1] == S[3])
    #print(T[2] > T[0] and S[2] == S[0] and T[2] > T[1] and S[2] == S[1] and T[2] > T[3] and S[2] == S[3])
    #print(T[3] > T[0] and S[3] == S[0] and T[3] > T[1] and S[3] == S[
