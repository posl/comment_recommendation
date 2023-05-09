def main():
    S = input()
    if len(S) < 2:
        print("No")
    elif len(S) == 2:
        if S[0] == S[1]:
            print("No")
        else:
            print("Yes")
    else:
        if S[0].islower() or S[1].islower():
            print("No")
        else:
            for i in range(2, len(S)):
                if S[i].islower():
                    print("No")
                    exit(0)
            print("Yes")
