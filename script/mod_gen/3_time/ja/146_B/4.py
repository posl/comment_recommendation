def main():
    n = int(input())
    s = input()
    for i in s:
        if ord(i) + n > ord('Z'):
            print(chr(ord(i) + n - ord('Z') + ord('A') - 1), end='')
        else:
            print(chr(ord(i) + n), end='')

if __name__ == '__main__':
    main()