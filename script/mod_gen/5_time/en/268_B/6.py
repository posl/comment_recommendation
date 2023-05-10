def main():
    s = input()
    t = input()
    if s == t[:len(s)]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()