def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, 26):
        if "".join([chr((ord(x) - ord("a") + i) % 26 + ord("a")) for x in S]) == T:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()