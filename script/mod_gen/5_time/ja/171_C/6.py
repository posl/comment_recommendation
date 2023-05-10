def main():
    N = int(input())
    N -= 1
    ans = ""
    while N >= 0:
        ans += chr(ord('a') + (N % 26))
        N = N // 26 - 1
    print(ans[::-1])

if __name__ == '__main__':
    main()