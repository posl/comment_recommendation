def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(1, 26):
        if s == ''.join([chr((ord(c) - ord('a') + i) % 26 + ord('a')) for c in t]):
            print('Yes')
            return
    print('No')
    return

if __name__ == '__main__':
    main()