def main():
    N = int(input())
    S = input()
    for c in S:
        print(chr((ord(c)-ord('A')+N)%26+ord('A')),end='')
    print()

if __name__ == '__main__':
    main()