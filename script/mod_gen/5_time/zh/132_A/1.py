def main():
    s = input()
    check = set(s)
    if len(check) == 2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()