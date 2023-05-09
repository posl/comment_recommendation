def main():
    H,W = map(int,input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    print(S)
    print(T)
    if H == 1:
        if S[0] == T[0]:
            print("Yes")
            return
        else:
            print("No")
            return
    if W == 1:
        for i in range(H):
            if S[i][0] != T[i][0]:
                print("No")
                return
        print("Yes")
        return
    S_ = []
    T_ = []
    for i in range(H):
        S_.append(list(S[i]))
        T_.append(list(T[i]))
    print(S_)
    print(T_)
    for i in range(W):
        for j in range(i+1,W):
            if S_[0][i] == S_[0][j]:
                if T_[0][i] == T_[0][j]:
                    continue
                else:
                    print("No")
                    return
            else:
                if T_[0][i] == T_[0][j]:
                    S_[0][i],S_[0][j] = S_[0][j],S_[0][i]
                    continue
                else:
                    print("No")
                    return
    print(S_)
    print(T_)
    for i in range(H):
        for j in range(W):
            if S_[i][j] == T_[i][j]:
                continue
            else:
                print("No")
                return
    print("Yes")
