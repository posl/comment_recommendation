def main():
    n = int(input())
    s = input()
    ans = []
    for i in s:
        ans.append(chr((ord(i) - ord('A') + n) % 26 + ord('A')))
    print(''.join(ans))

if __name__ == '__main__':
    main()