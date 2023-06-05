def main():
    s = input()
    count = 0
    while s != "0":
        if s[-1] == "0":
            s = s[:-1]
        else:
            s = str(int(s) - 1)
        count += 1
    print(count)

if __name__ == '__main__':
    main()