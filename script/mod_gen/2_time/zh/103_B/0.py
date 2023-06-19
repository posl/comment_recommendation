def main():
    S = input()
    T = input()
    if len(S) == len(T):
        for i in range(len(S)):
            S = S[1:] + S[0]
            if S == T:
                print("Yes")
                exit()
        print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()