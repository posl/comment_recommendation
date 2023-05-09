def solve():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    if S_len + 1 != T_len:
        print("No")
        return
    for i in range(S_len):
        if S[i] != T[i]:
            print("No")
            return
    print("Yes")
