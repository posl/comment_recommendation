def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    s_set = set(s)
    if len(s_set) != 2:
        print("No")
        return
    for c in s_set:
        if s.count(c) != 2:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()