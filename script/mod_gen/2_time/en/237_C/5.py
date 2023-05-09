def main():
    S = input()
    S_reverse = S[::-1]
    if S == S_reverse:
        print("Yes")
        return
    for i in range(len(S)):
        if S[i] != S_reverse[i]:
            if S[i:] == S_reverse[i:-1]:
                print("Yes")
                return
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()