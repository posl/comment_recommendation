def solve():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    if len(S) < len(T):
        print("No")
        return
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            S = S[:i + 1] + S[i] + S[i + 1:]
            if S == T:
                print("Yes")
                return
    print("No")
    return
