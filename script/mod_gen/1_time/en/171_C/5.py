def main():
    N = int(input())
    ans = []
    while N > 0:
        N -= 1
        ans.append(chr(N%26 + ord('a')))
        N //= 26
    print(''.join(ans[::-1]))

if __name__ == '__main__':
    main()