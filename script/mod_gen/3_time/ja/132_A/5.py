def main():
    S = input()
    S_set = set(S)
    if len(S_set) == 2:
        for i in S_set:
            if S.count(i) != 2:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()