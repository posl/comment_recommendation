def solve():
    S = input()
    T = input()
    #S = "abbaac"
    #T = "abbbbaaac"
    #S = "xyzz"
    #T = "xyyzz"
    if len(S) > len(T):
        print("No")
        return
    if len(S) == len(T):
        if S == T:
            print("Yes")
            return
        else:
            print("No")
            return
    i = 0
    j = 0
    while i < len(S):
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len(S):
        print("Yes")
    else:
        print("No")
    return
