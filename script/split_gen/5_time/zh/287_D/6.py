def main():
    S = input()
    T = input()
    lenS = len(S)
    lenT = len(T)
    for i in range(lenT+1):
        if i == 0:
            if S[lenT:lenS] == T:
                print("Yes")
            else:
                print("No")
        elif i == lenT:
            if S[0:lenT] == T:
                print("Yes")
            else:
                print("No")
        else:
            if S[i:lenT+i] == T:
                print("Yes")
            else:
                print("No")
