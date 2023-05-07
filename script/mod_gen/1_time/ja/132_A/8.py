def main():
    S = input()
    # S = "ASSA"
    # S = "STOP"
    # S = "FFEE"
    # S = "FREE"
    if len(S) == 4:
        if len(set(S)) == 2:
            if S.count(S[0]) == 2 and S.count(S[2]) == 2:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()