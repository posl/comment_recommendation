def main():
    S = input()
    if len(S) == 1:
        print("Yes")
        return
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i].islower() is False:
                print("No")
                return
        else:
            if S[i].isupper() is False:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()