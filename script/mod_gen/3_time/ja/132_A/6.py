def main():
    s = input()
    print('Yes' if len(set(s)) == 2 and s.count(s[0]) == 2 else 'No')

if __name__ == '__main__':
    main()