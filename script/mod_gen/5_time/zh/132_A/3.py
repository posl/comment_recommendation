def main():
    s = input()
    # print(s)
    if len(s) != 4:
        print("No")
        return
    if len(set(s)) != 2:
        print("No")
        return
    for i in set(s):
        if s.count(i) != 2:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()