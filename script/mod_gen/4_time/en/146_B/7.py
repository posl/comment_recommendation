def main():
    n = int(input())
    s = input()
    for i in s:
        print(chr((ord(i)-ord('A')+n)%26+ord('A')),end='')
    print()
main()

if __name__ == '__main__':
    main()