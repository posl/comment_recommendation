def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print('Won')
    else:
        print('Lost')

if __name__ == '__main__':
    main()