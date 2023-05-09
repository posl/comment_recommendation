def main():
    n = int(input())
    s = input()
    for i in s:
        print(chr((ord(i)-65+n)%26+65), end='')

if __name__ == '__main__':
    main()