def main():
    n = int(input())
    s = input()
    res = []
    for i in range(len(s)):
        if ord(s[i]) + n > ord('Z'):
            res.append(chr(ord(s[i]) + n - 26))
        else:
            res.append(chr(ord(s[i]) + n))
    print(''.join(res))

if __name__ == '__main__':
    main()