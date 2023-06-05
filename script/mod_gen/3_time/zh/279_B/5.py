def main():
    S = input()
    T = input()
    S_length = len(S)
    T_length = len(T)
    for i in range(S_length - T_length + 1):
        if S[i: i + T_length] == T:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()