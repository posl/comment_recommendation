def main():
    S = input()
    if S[0] == '0':
        print("No")
    else:
        if S[1] == '0' or S[2] == '0' or S[3] == '0' or S[4] == '0':
            print("No")
        else:
            if S[5] == '0' or S[6] == '0' or S[7] == '0' or S[8] == '0':
                print("No")
            else:
                print("Yes")
main()

if __name__ == '__main__':
    main()