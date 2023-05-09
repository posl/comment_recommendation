def main():
    s = input()
    if len(s) < 2:
        print("No")
        return
    if s.islower() or s.isupper():
        print("No")
        return
    if len(set(s)) != len(s):
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()