def main():
    S = input()
    if len(set(S)) != 2:
        print("No")
    elif S.count(S[0]) == 2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()