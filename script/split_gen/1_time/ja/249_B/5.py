def main():
    S = input()
    if len(S) >= 1 and len(S) <= 100:
        if S.isupper() and S.islower():
            print("No")
        elif S.isupper():
            print("No")
        elif S.islower():
            print("No")
        else:
            if len(S) == len(set(S)):
                print("Yes")
            else:
                print("No")
    else:
        print("No")
