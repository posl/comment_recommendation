def main():
    N = int(input())
    N -= 1
    ans = ''
    while N >= 0:
        ans += chr(N % 26 + ord('a'))
        N //= 26
        N -= 1
    print(ans[::-1])

if __name__ == '__main__':
    main()