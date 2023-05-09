def main():
    S = input()
    if S[0] == "0":
        print("No")
        return
    if S[1:4] == "000" and S[4:7] == "000" and S[7:10] == "000":
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()