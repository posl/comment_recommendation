def main():
    S = input()
    if S == "":
        print("Yes")
        return
    if S[0] == ")":
        print("No")
        return
    if S[-1] == "(":
        print("No")
        return
    if S.count("(") != S.count(")"):
        print("No")
        return
    if S.count("(") == 0:
        print("Yes")
        return
    if S.count(")") == 0:
        print("Yes")
        return
    if S.count("(") == 1 and S.count(")") == 1:
        print("Yes")
        return
    if S.count("(") == 1 and S.count(")") != 1:
        print("No")
        return
    if S.count("(") != 1 and S.count(")") == 1:
        print("No")
        return
    if S.count("(") == 2 and S.count(")") == 2:
        print("Yes")
        return
    if S.count("(") == 2 and S.count(")") != 2:
        print("No")
        return
    if S.count("(") != 2 and S.count(")") == 2:
        print("No")
        return
    if S.count("(") > 2 and S.count(")") > 2:
        if S[0] == "(" and S[-1] == ")":
            print("Yes")
            return
        if S[0] == "(" and S[-1] != ")":
            print("No")
            return
        if S[0] != "(" and S[-1] == ")":
            print("No")
            return
        if S[0] != "(" and S[-1] != ")":
            print("No")
            return

if __name__ == '__main__':
    main()