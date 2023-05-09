def main():
    S = input()
    if S.islower() or S.isupper():
        print("No")
    else:
        for i in range(len(S)):
            if S[i] in S[i+1:]:
                print("No")
                return
        print("Yes")

if __name__ == '__main__':
    main()