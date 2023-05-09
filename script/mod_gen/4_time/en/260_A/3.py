def main():
    str = input()
    print(str[0] if str[0] != str[1] and str[0] != str[2] else str[1] if str[1] != str[0] and str[1] != str[2] else str[2] if str[2] != str[0] and str[2] != str[1] else -1)

if __name__ == '__main__':
    main()