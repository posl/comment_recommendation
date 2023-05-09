def main():
    n = int(input())
    s = input()
    print(''.join([chr((ord(c)-ord('A')+n)%26+ord('A')) for c in s]))

if __name__ == '__main__':
    main()