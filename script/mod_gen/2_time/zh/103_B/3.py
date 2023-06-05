def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        if S == T:
            print("Yes")
            return
        S = S[-1] + S[0:-1]
    print("No")

if __name__ == '__main__':
    main()