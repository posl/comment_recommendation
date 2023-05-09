def main():
    H,W = map(int,input().split())
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]
    if H == 1:
        if S[0] == T[0]:
            print("Yes")
        else:
            print("No")
        return
    if W == 1:
        if S == T:
            print("Yes")
        else:
            print("No")
        return
    if H % 2 == 0 and W % 2 == 0:
        for i in range(H):
            if S[i] != T[i]:
                print("No")
                return
        print("Yes")
        return
    if H % 2 == 1 and W % 2 == 1:
        for i in range(H):
            if S[i] != T[i]:
                print("No")
                return
        print("Yes")
        return
    if H % 2 == 1 and W % 2 == 0:
        for i in range(H):
            if S[i] != T[i]:
                print("No")
                return
        print("Yes")
        return
    if H % 2 == 0 and W % 2 == 1:
        for i in range(H):
            if S[i] != T[i]:
                print("No")
                return
        print("Yes")
        return
