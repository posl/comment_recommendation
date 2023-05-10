def main():
    s = input()
    s = list(s)
    s.sort()
    if s[0] == '1':
        print(2)
    else:
        print(1)

if __name__ == '__main__':
    main()