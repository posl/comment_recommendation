def main():
    s = input()
    if s[0::2].count("R") == 0 and s[1::2].count("L") == 0:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()