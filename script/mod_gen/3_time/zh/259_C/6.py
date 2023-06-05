def solve():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    s = len(S)
    t = len(T)
    if t < s:
        print("No")
        return
    if s == 2:
        if S[0] == S[1]:
            if S[0] == T[0]:
                print("Yes")
                return
            elif S[0] == T[1]:
                print("Yes")
                return
            else:
                print("No")
                return
        else:
            print("No")
            return
    if s == 3:
        if S[0] == S[1] == S[2]:
            if S[0] == T[0]:
                print("Yes")
                return
            elif S[0] == T[1]:
                print("Yes")
                return
            elif S[0] == T[2]:
                print("Yes")
                return
            else:
                print("No")
                return
        elif S[0] == S[1]:
            if S[0] == T[0]:
                if S[2] == T[1]:
                    print("Yes")
                    return
                else:
                    print("No")
                    return
            elif S[0] == T[1]:
                if S[2] == T[2]:
                    print("Yes")
                    return
                else:
                    print("No")
                    return
            else:
                print("No")
                return
        elif S[1] == S[2]:
            if S[1] == T[1]:
                if S[0] == T[0]:
                    print("Yes")
                    return
                else:
                    print("No")
                    return
            elif S[1] == T[2]:
                if S[0] == T[0]:
                    print("Yes")
                    return
                else:
                    print("No")
                    return
            else:
                print("No")
                return
        else:
            print("No")
            return
    if s == 4:
        if S[0] == S[1] == S[2] == S[3]:
            if S[0] == T[0]:
                print("Yes")
                return
            elif S[0] == T[1]:
                print

if __name__ == '__main__':
    solve()