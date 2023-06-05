def main():
    S = input()
    if len(S) != 4:
        print("No")
        return
    if S[0] == S[1] and S[2] == S[3] and S[0] != S[2]:
        print("Yes")
        return
    if S[0] == S[2] and S[1] == S[3] and S[0] != S[1]:
        print("Yes")
        return
    if S[0] == S[3] and S[1] == S[2] and S[0] != S[1]:
        print("Yes")
        return
    print("No")

if __name__ == '__main__':
    main()