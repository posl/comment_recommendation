def main():
    S = input()
    T = input()
    for i in range(26):
        s = ""
        for j in range(len(S)):
            s += chr((ord(S[j]) - ord("a") + i) % 26 + ord("a"))
        if s == T:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()