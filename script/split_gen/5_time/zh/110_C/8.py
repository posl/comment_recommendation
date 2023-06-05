def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    #S = list(S)
    #T = list(T)
    #S.sort()
    #T.sort()
    #print(S)
    #print(T)
    Sdict = {}
    Tdict = {}
    for i in range(len(S)):
        if S[i] in Sdict:
            Sdict[S[i]] += 1
        else:
            Sdict[S[i]] = 1
        if T[i] in Tdict:
            Tdict[T[i]] += 1
        else:
            Tdict[T[i]] = 1
    #print(Sdict)
    #print(Tdict)
    Sdict = sorted(Sdict.items(), key=lambda x:x[1])
    Tdict = sorted(Tdict.items(), key=lambda x:x[1])
    #print(Sdict)
    #print(Tdict)
    for i in range(len(Sdict)):
        if Sdict[i][1] != Tdict[i][1]:
            print("No")
            return
    print("Yes")
    return
main()
