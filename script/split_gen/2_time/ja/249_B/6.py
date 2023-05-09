def main():
    S = input()
    if len(S) < 2:
        print("No")
        return
    if S.isupper():
        print("No")
        return
    if S.islower():
        print("No")
        return
    if S.isalpha() == False:
        print("No")
        return
    if len(S) != len(set(S)):
        print("No")
        return
    print("Yes")
