def solve():
    S = input()
    T = input()
    S1 = sorted(S)
    T1 = sorted(T)
    S2 = sorted(S1)
    T2 = sorted(T1)
    if S1 == T1 and S2 == T2:
        print("Yes")
    else:
        print("No")
