def solve():
    S = [input() for _ in range(3)]
    if len(S[0]) < len(S[1]):
        S[0], S[1] = S[1], S[0]
    if len(S[0]) < len(S[2]):
        S[0], S[2] = S[2], S[0]
    if len(S[1]) < len(S[2]):
        S[1], S[2] = S[2], S[1]
    if len(S[0]) == len(S[1]) + len(S[2]):
        if len(S[1]) < len(S[2]):
            S[1], S[2] = S[2], S[1]
        if len(S[0]) == 1 and len(S[1]) == 1 and len(S[2]) == 1:
            print(1)
            print(1)
            print(2)
            return
        if S[0][0] == S[1][0] or S[0][0] == S[2][0]:
            print("UNSOLVABLE")
            return
        if len(S[0]) == len(S[1]) == len(S[2]):
            if S[0][0] == S[1][0] or S[0][0] == S[2][0]:
                print("UNSOLVABLE")
                return
            if S[0][1] == S[1][1] or S[0][1] == S[2][1]:
                print("UNSOLVABLE")
                return
            if S[0][2] == S[1][2] or S[0][2] == S[2][2]:
                print("UNSOLVABLE")
                return
            print(1)
            print(1)
            print(2)
            return
        print("UNSOLVABLE")
        return
    if len(S[0]) == len(S[1]):
        if len(S[0]) == 1 and len(S[1]) == 1 and len(S[2]) == 1:
            print(1)
            print(1)
            print(2)
            return
        if S[0][0] == S[1][0]:
            print("UNSOLVABLE")
            return
