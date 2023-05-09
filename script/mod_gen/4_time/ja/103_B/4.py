def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        S = S[1:] + S[0]
        if S == T:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()