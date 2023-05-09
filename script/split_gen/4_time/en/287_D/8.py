def solve():
    S = input()
    T = input()
    s = len(S)
    t = len(T)
    S = S.replace("?","a")
    for i in range(s-t,-1,-1):
        if T == S[i:i+t]:
            S = S[:i] + T + S[i+t:]
            S = S.replace("?","a")
            print("Yes")
            return
    print("No")
    return
