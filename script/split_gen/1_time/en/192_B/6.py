def main():
    S = input()
    if S[0].islower():
        for i in range(1, len(S), 2):
            if S[i].isupper():
                continue
            else:
                print("No")
                return
        for i in range(2, len(S), 2):
            if S[i].islower():
                continue
            else:
                print("No")
                return
    else:
        for i in range(1, len(S), 2):
            if S[i].islower():
                continue
            else:
                print("No")
                return
        for i in range(2, len(S), 2):
            if S[i].isupper():
                continue
            else:
                print("No")
                return
    print("Yes")
