def main():
    S = input()
    if len(S) == 4:
        if S.count(S[0]) == 2 and S.count(S[1]) == 2 and S.count(S[2]) == 2 and S.count(S[3]) == 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
