def main():
    S = input()
    S_list = list(S)
    S_set = set(S_list)
    if len(S_set) == 2:
        for i in S_set:
            if S_list.count(i) != 2:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()