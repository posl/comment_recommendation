def main():
    S = input()
    T = input()
    if len(S) == len(T):
        for i in range(len(S)):
            if S[i] != T[i]:
                if (ord(S[i]) + 1) % 97 == ord(T[i]) % 97:
                    pass
                else:
                    print("No")
                    exit()
        print("Yes")
    else:
        print("No")
main()
