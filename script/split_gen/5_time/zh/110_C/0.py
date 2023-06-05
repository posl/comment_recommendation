def solve():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    S = list(S)
    T = list(T)
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        else:
            for j in range(i+1,len(S)):
                if S[j] == S[i]:
                    S[j] = T[i]
                elif S[j] == T[i]:
                    S[j] = S[i]
            S[i] = T[i]
    if S == T:
        print("Yes")
        return
    else:
        print("No")
        return
