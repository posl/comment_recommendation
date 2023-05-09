def main():
    S = input()
    if len(S) < 2:
        print("No")
        return
    if S.islower():
        print("No")
        return
    if S.isupper():
        print("No")
        return
    if not S.isalpha():
        print("No")
        return
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            if S[i] == S[j]:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()