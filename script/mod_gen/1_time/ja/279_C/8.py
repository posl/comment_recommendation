def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    if H==1:
        if "".join(S)=="".join(T):
            print("Yes")
        else:
            print("No")
        return
    if W==1:
        if "".join(S)=="".join(T):
            print("Yes")
        else:
            print("No")
        return
    if H==2:
        for i in range(W):
            if S[0][i]+S[1][i]==T[0][i]+T[1][i]:
                continue
            else:
                print("No")
                return
        print("Yes")
        return
    if W==2:
        for i in range(H):
            if S[i][0]+S[i][1]==T[i][0]+T[i][1]:
                continue
            else:
                print("No")
                return
        print("Yes")
        return
    if H==3:
        for i in range(W):
            if S[0][i]+S[1][i]+S[2][i]==T[0][i]+T[1][i]+T[2][i]:
                continue
            else:
                print("No")
                return
        print("Yes")
        return
    if W==3:
        for i in range(H):
            if S[i][0]+S[i][1]+S[i][2]==T[i][0]+T[i][1]+T[i][2]:
                continue
            else:
                print("No")
                return
        print("Yes")
        return
    if H==4:
        for i in range(W):
            if S[0][i]+S[1][i]+S[2][i]+S[3][i]==T[0][i]+T[1][i]+T[2][i]+T[3][i]:
                continue
            else:
                print("No")
                return
        print("Yes")
        return
    if W==4:
        for i in range(H):
            if S[i][0]+S[i][1]+S[i][2]+S[i][3]==T[i][0]+T[i][1]+T[i][2]+T[i][3]:
                continue

if __name__ == '__main__':
    main()