def solve():
    S = input()
    S1 = S
    S2 = S
    for i in range(len(S)):
        S1 = S1[1:] + S1[0]
        S2 = S2[-1] + S2[0:-1]
        if S1 < S2:
            print(S1)
            print(S2)
            break
        elif S1 > S2:
            print(S2)
            print(S1)
            break
        else:
            continue
solve()
