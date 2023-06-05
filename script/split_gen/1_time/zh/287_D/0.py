def main():
    S = input()
    T = input()
    #print(S,T)
    for x in range(len(T)+1):
        S_ = S[:x] + S[len(S) - len(T) + x:]
        #print(S_)
        flag = True
        for i in range(len(T)):
            if S_[i] == "?":
                continue
            if S_[i] != T[i]:
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")
