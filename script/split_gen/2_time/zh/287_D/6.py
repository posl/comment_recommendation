def main():
    S = input()
    T = input()
    lenS = len(S)
    lenT = len(T)
    for x in range(lenT+1):
        S1 = S[0:x] + S[lenS-lenT+x:lenS]
        if len(S1) == len(T):
            flag = True
            for i in range(lenT):
                if S1[i] != T[i] and S1[i] != "?":
                    flag = False
                    break
            if flag:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
