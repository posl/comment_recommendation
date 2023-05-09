def main():
    S = input()
    if len(S) < 2:
        print("No")
        return
    if S[0].isupper() and S[1].islower():
        for i in range(2, len(S)):
            if S[i].isupper():
                print("No")
                return
    else:
        print("No")
        return
    if len(set(S)) == len(S):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()