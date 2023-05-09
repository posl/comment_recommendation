def main():
    S = input()
    if len(S) != len(set(S)):
        print("No")
        return
    if S.islower() or S.isupper():
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()