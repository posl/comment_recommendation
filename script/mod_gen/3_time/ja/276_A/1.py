def main():
    s = input()
    if 'a' in s:
        print(len(s) - s[::-1].index('a'))
    else:
        print(-1)
main()

if __name__ == '__main__':
    main()