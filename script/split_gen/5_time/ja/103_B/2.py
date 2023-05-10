def solve():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    else:
        for i in range(len(S)):
            S = S[-1] + S[0:-1]
            if S == T:
                print("Yes")
                return
    print("No")
    return
