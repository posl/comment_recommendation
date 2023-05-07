def main():
    S = input()
    if (S.isupper() or S.islower()):
        print("No")
    elif (len(S) == len(set(S))):
        print("Yes")
    else:
        print("No")
main()
