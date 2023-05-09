def main():
    S = input()
    if S[0] == '1':
        print("No")
        return
    if S[1] == '1' and S[2] == '1' and S[3] == '1' and S[4] == '1':
        print("No")
        return
    if S[5] == '1' and S[6] == '1' and S[7] == '1' and S[8] == '1':
        print("No")
        return
    if S[1] == '1' and S[5] == '1':
        print("Yes")
        return
    if S[2] == '1' and S[6] == '1':
        print("Yes")
        return
    if S[3] == '1' and S[7] == '1':
        print("Yes")
        return
    if S[4] == '1' and S[8] == '1':
        print("Yes")
        return
    print("No")
main()

if __name__ == '__main__':
    main()