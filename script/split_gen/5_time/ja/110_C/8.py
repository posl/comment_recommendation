def main():
    S = input()
    T = input()
    #print("S:",S)
    #print("T:",T)
    #print("len(S):",len(S))
    #print("len(T):",len(T))
    if len(S) != len(T):
        print("No")
        return
    if len(S) == 1:
        if S == T:
            print("Yes")
        else:
            print("No")
        return
    Sdic = {}
    Tdic = {}
    for i in range(len(S)):
        if S[i] in Sdic:
            Sdic[S[i]] += 1
        else:
            Sdic[S[i]] = 1
        if T[i] in Tdic:
            Tdic[T[i]] += 1
        else:
            Tdic[T[i]] = 1
    #print("Sdic:",Sdic)
    #print("Tdic:",Tdic)
    if len(Sdic) != len(Tdic):
        print("No")
        return
    for i in range(len(S)):
        if S[i] != T[i]:
            if Sdic[S[i]] != Tdic[S[i]]:
                print("No")
                return
    print("Yes")
