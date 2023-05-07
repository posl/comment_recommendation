def main():
    s = input()
    a = []
    for i in s:
        if i not in a:
            a.append(i)
    if len(a) == 2:
        for i in a:
            if s.count(i) == 2:
                print("Yes")
            else:
                print("No")
                break
    else:
        print("No")

if __name__ == '__main__':
    main()