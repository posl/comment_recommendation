def main():
    s = input()
    t = input()
    if s == t[0:len(s)]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()