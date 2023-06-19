def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
    else:
        for i in range(len(S)):
            if ord(S[i]) != ord(T[i]) and (ord(S[i]) + 1) != ord(T[i]):
                print("No")
                break
        else:
            print("Yes")

if __name__ == '__main__':
    main()