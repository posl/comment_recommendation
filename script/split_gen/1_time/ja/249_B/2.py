def main():
    S = input()
    if S.isupper() or S.islower():
        print("No")
        return
    if len(S) != len(set(S)):
        print("No")
        return
    print("Yes")
