def main():
    S = input()
    if len(set(S)) == 2:
        if S.count(S[0]) == 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()