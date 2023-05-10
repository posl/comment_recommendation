def main():
    S = input()
    if S[0] == "0":
        print("No")
        return
    if S[4] == "0" and S[5] == "0":
        print("No")
        return
    if S[6] == "0" and S[7] == "0":
        print("No")
        return
    if S[8] == "0" and S[9] == "0":
        print("No")
        return
    print("Yes")
    return

if __name__ == '__main__':
    main()