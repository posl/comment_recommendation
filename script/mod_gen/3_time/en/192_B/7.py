def main():
    S = input()
    if len(S) == 1:
        print("Yes")
        return
    if S[0].isupper() or S[1].islower():
        print("No")
        return
    for i in range(2, len(S)):
        if i % 2 == 0:
            if S[i].islower():
                print("No")
                return
        else:
            if S[i].isupper():
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()