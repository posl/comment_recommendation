def main():
    s = input()
    if len(s) == 4:
        if len(set(s)) == 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()