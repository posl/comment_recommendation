def main():
    S = input()
    if len(S) < 3:
        print("No")
        return
    if not S[0].isupper():
        print("No")
        return
    if not S[-1].isupper():
        print("No")
        return
    if not S[1:-1].isdigit():
        print("No")
        return
    if not (100000 <= int(S[1:-1]) <= 999999):
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()