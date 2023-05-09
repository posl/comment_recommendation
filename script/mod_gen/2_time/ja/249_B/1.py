def main():
    S = input()
    if S.islower() or S.isupper():
        print("No")
    elif len(S) != len(set(S)):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()