def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    for c in s:
        if s.count(c) != 2:
            print("No")
            return
    print("Yes")
    return
main()
