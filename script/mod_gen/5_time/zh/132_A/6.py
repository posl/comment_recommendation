def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    if len(set(s)) != 2:
        print("No")
        return
    for c in set(s):
        if s.count(c) != 2:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()