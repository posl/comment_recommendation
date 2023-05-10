def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S_ = []
    S_.append(S[0])
    for i in range(1,N):
        if S[i] in S_:
            S_.append(S[i]+"("+str(S_.count(S[i]))+")")
        else:
            S_.append(S[i])
    for i in range(N):
        print(S_[i])
main()
