def main():
    s = input()
    y = int(s[0:4])
    m = int(s[5:7])
    d = int(s[8:])
    if y < 2019:
        print("Heisei")

if __name__ == '__main__':
    main()