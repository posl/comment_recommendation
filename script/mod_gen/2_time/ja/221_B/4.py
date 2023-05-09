def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S) - 1):
            S = S[:i] + S[i + 1] + S[i] + S[i + 2:]
            if S == T:
                print("Yes")
                break
            S = S[:i] + S[i + 1] + S[i] + S[i + 2:]
        else:
            print("No")

if __name__ == '__main__':
    main()